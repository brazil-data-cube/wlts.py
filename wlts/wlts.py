#
# This file is part of Python Client Library for the WLTS.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#
"""Python Client Library for WLTS.

This module introduces a class named ``WLTS`` that can be used to retrieve
trajectories for a given location.
"""
import json
from typing import Dict

import httpx
import lccs
import numpy as np
import requests

from .collection import Collections
from .trajectories import Trajectories
from .trajectory import Trajectory
from .utils import Utils


class WLTS:
    """This class implement a client for WLTS.

    .. note::
        For more information about WLTS, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, url, lccs_url=None, access_token=None, language=None):
        """Create a WLTS client attached to the given host address (an URL).

        Args:
            url (str): URL for the WLTS server.
            lccs_url (str, optional): URL for the LCCS server.
            access_token (str, optional): Authentication token to be used with the WLTS server.
        """
        #: str: URL for the WLTS server.
        self._url = url if url[-1] != "/" else url[0:-1]

        #: str: Authentication token to be used with the WLTS server.
        self._access_token: str = access_token or ""
        self._headers: Dict[str, str] = (
            {"x-api-key": self._access_token} if self._access_token else {}
        )

        self._language: str = language or "pt-br"

        #: str: URL for the LCCS server.
        self._lccs_url = (
            lccs_url if lccs_url else "https://data.inpe.br/bdc/lccs/v1"
        )

        self.lccs_service = lccs.LCCS(
            url=self._lccs_url, 
            language=self._language,
            access_token=self._access_token
        )

    @property
    def collections(self):
        """Return a list of collections names.

        Returns:
            list: A list with the names of available collections in the service.

        Raises:
            ConnectionError: If the server is not reachable.
            HTTPError: If the server response indicates an error.
            ValueError: If the response body is not a json document.
        """
        return self._list_collections()

    def _support_language(self):
        """Returns the languages supported by the service."""
        import enum

        response = requests.get(f"{self._url}/")

        response.raise_for_status()

        data = response.json()

        return enum.Enum(
            "Language",
            {i["language"]: i["language"] for i in data["supported_language"]},
            type=str,
        )

    def tj(self, latitude, longitude, **options):
        """Retrieve the trajectory for a given location and time interval.

        Keyword Args:
            collections (optional): A string with collections names separated by commas,
            or any sequence of strings. If omitted, the values for all collections are retrieved.
            longitude (float/int/list/ndarray): Longitude(s) in EPSG:4326.
            latitude (float/int/list/ndarray): Latitude(s) in EPSG:4326.
            start_date (:obj:`str`, optional): The begin of a time interval.
            end_date (:obj:`str`, optional): The end of a time interval.
            geometry (:obj:`str`, optional): A string that accepted True or False.
            language (:obj:`str`, optional): The language of classes.

        Returns:
            Trajectory or Trajectories
        """

        def validate_lat_long(lat, long):
            if not isinstance(
                lat, (float, int, np.floating, np.integer)
            ) or not isinstance(long, (float, int, np.floating, np.integer)):
                raise ValueError("Arguments latitude and longitude must be numeric.")
            if (lat < -90.0) or (lat > 90.0):
                raise ValueError("latitude is out-of range [-90,90]!")
            if (long < -180.0) or (long > 180.0):
                raise ValueError("longitude is out-of range [-180,180]!")

        invalid_parameters = set(options) - {
            "start_date",
            "end_date",
            "collections",
            "geometry",
            "target_system",
            "language",
        }

        if invalid_parameters:
            raise AttributeError("invalid parameter(s): {}".format(invalid_parameters))

        if "language" in options:
            self._support_l = self._support_language()
            if options["language"] not in [e.value for e in self._support_l]:
                s = ", ".join([e for e in self.allowed_language])
                raise KeyError(f"Language not supported! Use: {s}")

        if "collections" in options and not isinstance(options["collections"], str):
            options["collections"] = ",".join(options["collections"])

        is_scalar = isinstance(
            latitude, (float, int, np.floating, np.integer)
        ) and isinstance(longitude, (float, int, np.floating, np.integer))

        if is_scalar:
            validate_lat_long(latitude, longitude)

            data = self._trajectory(
                **{
                    "latitude": float(latitude),
                    "longitude": float(longitude),
                    **options,
                }
            )

            for trj in data["result"]["trajectory"]:
                trj["point_id"] = 1

            if "target_system" in options:
                j = self._harmonize(
                    data["result"]["trajectory"], target_system=options["target_system"]
                )
                data["result"]["trajectory"] = json.loads(j)
                return Trajectory(data)

            return Trajectory(data)

        if isinstance(latitude, np.ndarray):
            latitude = latitude.tolist()
        if isinstance(longitude, np.ndarray):
            longitude = longitude.tolist()

        if not isinstance(latitude, list) or not isinstance(longitude, list):
            raise ValueError(
                "latitude and longitude must be float, int, list, or numpy.ndarray"
            )

        if len(latitude) != len(longitude):
            raise ValueError("latitude and longitude must have the same length")

        result = []
        index = 1

        for lat, long in zip(latitude, longitude):
            validate_lat_long(lat, long)

            data = self._trajectory(
                **{"latitude": float(lat), "longitude": float(long), **options}
            )

            for trj in data["result"]["trajectory"]:
                trj["point_id"] = index

            index += 1
            result.append(Trajectory(data))

        return Trajectories({"trajectories": result})

    def _harmonize(self, data, target_system):
        """Harmonize the trajectories into target classification system."""
        import pandas as pd

        lccs_service = lccs.LCCS(url=self._lccs_url, access_token=self._access_token)

        df = pd.DataFrame(data)

        for i in df["collection"].unique():
            ds = self._describe_collection(i)
            mappings = lccs_service.mappings(
                system_source=f"{ds['classification_system']['id']}",
                system_target=target_system,
            )
            for map in mappings.mappings:
                df.loc[
                    (df["collection"] == i) & (df["class"] == map.source_class.title),
                    ["class"],
                ] = map.target_class.title

        return df.to_json()

    def _list_collections(self):
        """Return the list of available collections."""
        result = self._get(self._url, op="list_collections")

        return result["collections"]

    def _trajectory(self, **params):
        """Retrieve the trajectories of collections associated with a given location in space.

        Retrieve the land use and cover trajectory associated to the
        informed location considering the given date interval and the
        collections.

        Keyword Args:
            collections (optional): A string with collections names separated by commas,
            or any sequence of strings. If omitted, the values for all collections are retrieved.
            longitude (int/float): A longitude value according to EPSG:4326.
            latitude (int/float): A latitude value according to EPSG:4326.
            start_date (:obj:`str`, optional): The begin of a time interval.
            end_date (:obj:`str`, optional): The end of a time interval.
            geometry (:obj:`str`, optional): A string that accepted True of False.

         Returns:
            Trajectory: A trajectory object as a dictionary.
        """
        return self._get(self._url, op="trajectory", **params)

    def _describe_collection(self, collection_id):
        """Describe a give collection.

        :param collection_id: The collection name.
        :type collection_id: str.

        :returns: Collection description.
        :rtype: dict
        """
        return self._get(
            self._url, op="describe_collection", collection_id=collection_id
        )

    def __getitem__(self, key):
        """Get collection whose name is identified by the key.

        Returns:
            Collection: A collection metadata object.

        Example:
            Get a collection object named ``deter_amazonia_legal``:

            .. doctest::
                :skipif: WLTS_EXAMPLE_URL is None

                >>> from wlts import *
                >>> service = WLTS(WLTS_EXAMPLE_URL)
                >>> service['deter_amazonia_legal']
                Collection...
        """
        cv_meta = self._describe_collection(key)

        return Collections(service=self, metadata=cv_meta)

    @property
    def url(self):
        """Return the WLTS server instance URL."""
        return self._url

    def build_color_dict(self, collections) -> dict:
        """Build colors from lccs."""
        color_maps = {}

        for collection in collections:
            describe_collection = self._describe_collection(collection)

            system_id = describe_collection["classification_system"].get("id")

            classification_system = self.lccs_service.classification_system(system=system_id)

            color_maps[collection] = {
                cv.title: cv.color
                for cv in classification_system.classes(style_format_name_or_id="SLD-Feature-Point")
            }

        return color_maps

    def plot(self, dataframe, **parameters):
        """Plot the trajectory on a scatter or bar plot.

        Args:
            dataframe (pandas.DataFrame): The trajectory as dataframe representation.

        Keyword Args:
            marker_size (int): The marker size .
            title (str): The title. Ex: Land Use and Cover Trajectory.
            title_y (str): The title in the y-axis. Ex: Number of Points.
            date (str): Title of date. Ex: Year.
            value (str): The label of value. Ex: Collection.
            width (int): The width size.
            height (int): The height size.
            font_size (int): The font size.
            type (str): The graphic type: scatter or bar.
            textfont_size (int): The text font size.
            textangle (int): The text angle. Ex: 0.
            textposition (str): Specifies the location of the text. Like “inside
            cliponaxis (bool): Determines whether the text nodes are clipped abo
            text_auto (bool): Determines  the display of text.
            textposition (str): Specifies the location of the text.
            opacity (float): The text opacity.
            marker_line_width (float): The marker line width.
            bar_title (bool): Update the title with spaces and letter uppercase.

        Raises:
            ImportError: If plotly could not be imported.

        """
        try:
            import plotly.express as px
        except ImportError:
            raise ImportError("You should install Plotly!")

        # Defaults
        parameters.setdefault("marker_size", 10)
        parameters.setdefault("title", "Land Use and Cover Trajectory")
        parameters.setdefault("title_y", "Number of Points")
        parameters.setdefault("legend_title_text", "Class")
        parameters.setdefault("date", "Year")
        parameters.setdefault("value", "Collection")
        parameters.setdefault("width", 950)
        parameters.setdefault("height", 320)
        parameters.setdefault("font_size", 12)
        parameters.setdefault("type", "scatter")

        # Traces defaults
        parameters.setdefault("textfont_size", 12)
        parameters.setdefault("textangle", 0)
        parameters.setdefault("textposition", "auto")
        parameters.setdefault("cliponaxis", False)

        # Layout defaults
        parameters.setdefault("text_auto", True)
        parameters.setdefault("opacity", 0.8)
        parameters.setdefault("marker_line_width", 1.5)

        df = dataframe.copy()
        df["class"] = df["class"].astype("category")
        df["date"] = df["date"].astype("category")
        df["collection"] = df["collection"].astype("category")

        # 🔑 Resolve o color_dict sempre aqui
        color_dict = parameters.get("color_dict")
        if not (color_dict and any(color_dict.values())):
            color_dict = self.build_color_dict(
                collections=list(df["collection"].unique())
            )

        # --- Scatter ---
        if parameters["type"] == "scatter":
            if len(df.point_id.unique()) == 1:
                df["label"] = (
                    df["collection"].astype(str) + " - " + df["class"].astype(str)
                )

                # Achata dicionário coleção+classe -> cor
                color_discrete_map = {
                    f"{collection} - {class_name}": color
                    for collection, classes in color_dict.items()
                    for class_name, color in classes.items()
                }

                fig = px.scatter(
                    df,
                    x="date",
                    y="collection",
                    color="label",
                    color_discrete_map=color_discrete_map,
                    labels={
                        "date": parameters["date"],
                        "collection": parameters["value"],
                    },
                    title=parameters["title"],
                    width=parameters["width"],
                    height=parameters["height"],
                )

                fig.update_traces(marker_size=parameters["marker_size"])
                fig.update_layout(
                    legend_title_text=parameters["legend_title_text"],
                    font=dict(size=parameters["font_size"]),
                )
                return fig
            else:
                raise ValueError(
                    "The scatter plot is for one point only! Please try another type: bar plot."
                )

        # --- Bar (uma coleção) ---
        if parameters["type"] == "bar":
            if len(df.collection.unique()) == 1 and len(df.point_id.unique()) >= 1:
                df_group = df.groupby(["date", "class"]).count()["point_id"].unstack()

                collection = df.collection.unique()[0]
                color_discrete_map = color_dict.get(collection, None)

                fig = px.bar(
                    df_group,
                    title=parameters["title"],
                    width=parameters["width"],
                    height=parameters["height"],
                    labels={"date": parameters["date"], "value": parameters["title_y"]},
                    text_auto=parameters["text_auto"],
                    color_discrete_map=color_discrete_map,
                )

                fig.update_layout(
                    legend_title_text=parameters["legend_title_text"],
                    font=dict(size=parameters["font_size"]),
                )
                fig.update_traces(
                    textfont_size=parameters["textfont_size"],
                    textangle=parameters["textangle"],
                    textposition=parameters["textposition"],
                    cliponaxis=parameters["cliponaxis"],
                    opacity=parameters["opacity"],
                    marker_line_width=parameters["marker_line_width"],
                )
                return fig

            # --- Bar (várias coleções) ---
            elif len(df.collection.unique()) >= 1 and len(df.point_id.unique()) >= 1:
                df_group = (
                    df.groupby(["collection", "date", "class"], observed=False)
                    .agg(count=("point_id", "count"))
                    .reset_index()
                )

                # Junta todos os dicionários de classes em um só
                color_discrete_map = {}
                for classes in color_dict.values():
                    color_discrete_map.update(classes)

                fig = px.bar(
                    df_group,
                    x="date",
                    y="count",
                    color="class",
                    facet_col="collection",
                    title=parameters["title"],
                    width=parameters["width"],
                    height=parameters["height"],
                    labels={
                        "date": parameters["date"],
                        "count": parameters["title_y"],
                        "class": parameters["legend_title_text"],
                    },
                    text="count",
                    text_auto=parameters["text_auto"],
                    color_discrete_map=color_discrete_map or None,
                )

                fig.update_layout(
                    legend_title_text=parameters["legend_title_text"],
                    font=dict(size=parameters["font_size"]),
                )
                fig.update_traces(
                    textfont_size=parameters["textfont_size"],
                    textangle=parameters["textangle"],
                    textposition=parameters["textposition"],
                    cliponaxis=parameters["cliponaxis"],
                    opacity=parameters["opacity"],
                    marker_line_width=parameters["marker_line_width"],
                )
                return fig

        raise RuntimeError("No plot support for this trajectory!")


    def __str__(self):
        """Return the string representation of the WLTS object."""
        text = f"WLTS:\n\tURL: {self._url}"

        return text

    def __repr__(self):
        """Return the WTLS object representation."""
        text = f'wlts(url="{self._url}")'

        return text

    def __iter__(self):
        """Iterate over collections available in the service.

        Returns:
            A collection at each iteration.
        """
        for cl_name in self.collections:
            yield self[cl_name]

    def _repr_html_(self):
        """Display the WLTS object as HTML.

        This integrates a rich display in IPython.
        """
        cl_list = self._list_collections()

        html = Utils.render_html("wlts.html", url=self._url, collections=cl_list)

        return html

    def _get(self, url, op, **params):
        """Query the WLTS service using HTTP GET verb and return the result as a JSON document.

        :param url: The URL to query must be a valid WLTS endpoint.
        :type url: str

        :param op: WLTS operation.
        :type url: str

        :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the underlying `Requests`.
        :type params: dict

        :rtype: dict

        :raises ValueError: If the response body does not contain a valid json.
        """
        url = f"{self._url}/{op}"
        params.setdefault("access_token", self._access_token)

        with httpx.Client() as client:
            response = client.get(url, params=params, headers=self._headers)
            response.raise_for_status()

        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            raise ValueError(f"HTTP Response is not JSON: Content-Type: {content_type}")

        return response.json()
