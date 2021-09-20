#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for WLTS."""
import json

import lccs
import requests

from .collection import Collections
from .trajectories import Trajectories
from .trajectory import Trajectory
from .utils import Utils


class WLTS:
    """This class implements a Python API client wrapper for WLTS.

    .. note::
        For more information about WLTS, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, url, lccs_url=None, access_token=None):
        """Create a WLTS client attached to the given host address (an URL).

        Args:
            url (str): URL for the WLTS server.
            access_token (str, optional): Authentication token to be used with the WLTS server.
        """
        self._url = url if url[-1] != '/' else url[0:-1]
        self._access_token = access_token
        self._lccs_url = lccs_url if lccs_url else 'https://brazildatacube.dpi.inpe.br/dev/lccs'

    @property
    def collections(self):
        """Return a list of collections names.

        Returns:
            list: A list with the names of available collections in the service.
        """
        return self._list_collections()

    def tj(self, latitude, longitude, **options):
        """Retrieve the trajectory for a given location and time interval.

        Keyword Args:
            collections (optional): A string with collections names separated by commas,
            or any sequence of strings. If omitted, the values for all collections are retrieved.
            longitude (int/float/list): A longitude value according to EPSG:4326.
            latitude (int/float/list): A latitude value according to EPSG:4326.
            start_date (:obj:`str`, optional): The begin of a time interval.
            end_date (:obj:`str`, optional): The end of a time interval.
            geometry (:obj:`str`, optional): A string that accepted True of False.

        Returns:
            Trajectory: A trajectory object as a dictionary.

        Example:

            Retrieves a trajectory:

            .. doctest::
                :skipif: WLTS_EXAMPLE_URL is None

                >>> from wlts import *
                >>> service = WLTS(WLTS_EXAMPLE_URL)
                >>> tj = service.tj(latitude=-12.0, longitude=-54.0, collections='mapbiomas_amazonia-v5,terraclass_amazonia', target_system='terraclass_amazonia')
                >>> ts.trajectory
                [{'class': 'Formação Florestal', 'collection': 'mapbiomas5_amazonia', 'date': '2007'}]
        """
        def validate_lat_long(lat, long):
            if (type(lat) not in (float, int)) or (type(long) not in (float, int)):
                raise ValueError("Arguments latitude and longitude must be numeric.")

            if (lat < -90.0) or (lat > 90.0):
                raise ValueError('latitude is out-of range [-90,90]!')

            if (long < -180.0) or (long > 180.0):
                raise ValueError('longitude is out-of range [-180,180]!')

        invalid_parameters = set(options) - {"start_date", "end_date", "collections", "geometry", "target_system"}

        if invalid_parameters:
            raise AttributeError('invalid parameter(s): {}'.format(invalid_parameters))

        if type(latitude) != list and type(longitude) != list:
            validate_lat_long(latitude, longitude)

            data = self._trajectory(**{'latitude': latitude, 'longitude': longitude, **options})

            if "target_system" in options:
                j = self._harmonize(data['result']['trajectory'], target_system=options["target_system"])
                data['result']['trajectory'] = json.loads(j)

                return Trajectory(data)

            return Trajectory(data)

        result = list()

        for lat, long in zip(latitude, longitude):
            validate_lat_long(lat, long)

            data = self._trajectory(**{'latitude': lat, 'longitude': long, **options})

            result.append(Trajectory(data))

        return Trajectories({"trajectories": result})

    def _harmonize(self, data, target_system):
        import pandas as pd

        lccs_service = lccs.LCCS(url=self._lccs_url, access_token=self._access_token)
        df = pd.DataFrame(data)

        for i in df['collection'].unique():
            ds = self._describe_collection(i)
            mappings = lccs_service.mappings(
                system_name_source=f"{ds['classification_system']['classification_system_name']}-{ds['classification_system']['classification_system_version']}",
                system_name_target=target_system)

            for map in mappings.mapping:
                df.loc[(df['collection'] == i) & (df["class"] == map.source_class.name), ['class']] = map.target_class.name

        return df.to_json()

    def _list_collections(self):
        """Return the list of available collections."""
        result = self._get(self._url, op='list_collections')

        return result['collections']

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
        return self._get(self._url, op='trajectory', **params)

    def _describe_collection(self, collection_id):
        """Describe a give collection.

        :param collection_id: The collection name.
        :type collection_id: str.

        :returns: Collection description.
        :rtype: dict
        """
        return self._get(self._url, op='describe_collection', collection_id=collection_id)

    def __getitem__(self, key):
        """Get collection whose name is identified by the key.

        Returns:
            Collection: A collection metadata object.

        Example:
            Get a collection object named ``deter_amz_legal``:

            .. doctest::
                :skipif: WLTS_EXAMPLE_URL is None

                >>> from wlts import *
                >>> service = WLTS(WLTS_EXAMPLE_URL)
                >>> service['deter_amz_legal']
                Collection...
        """
        cv_meta = self._describe_collection(key)

        return Collections(service=self, metadata=cv_meta)

    @property
    def url(self):
        """Return the WLTS server instance URL."""
        return self._url

    def __str__(self):
        """Return the string representation of the WLTS object."""
        text = f'WLTS:\n\tURL: {self._url}'

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

        html = Utils.render_html('wlts.html', url=self._url, collections=cl_list)

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
        url_components = [url, op]

        params.setdefault('access_token', self._access_token)

        url = '/'.join(s.strip('/') for s in url_components)

        response = requests.get(url, params=params)

        response.raise_for_status()

        content_type = response.headers.get('content-type')

        if content_type.count('application/json') == 0:
            raise ValueError(f'HTTP response is not JSON: Content-Type: {content_type}')

        return response.json()
