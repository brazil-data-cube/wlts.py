#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019-2020 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for WLTS."""

import requests

from .collection import Collections
from .trajectory import Trajectory


class WLTS:
    """This class implements a Python API client wrapper for WLTS.

    .. note::
        For more information about WLTS, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.

    :param url: The WLTS server URL.
    :type url: str
    """

    def __init__(self, url):
        """Create a WLTS client attached to the given host address (an URL)."""
        self._url = url if url[-1] != '/' else url[0:-1]

    @property
    def collections(self):
        """Return a list of collections names.

        Returns:
            list: A list with the names of available collections in the service.
        """
        return self._list_collections()

    def tj(self, **options):
        """Retrieve the trajectory for a given location and time interval.

        Keyword Args:
            collections (optional): A string with collections names separated by commas,
            or any sequence of strings. If omitted, the values for all collections are retrieved.
            longitude (int/float): A longitude value according to EPSG:4326.
            latitude (int/float): A latitude value according to EPSG:4326.
            start_date (:obj:`str`, optional): The begin of a time interval.
            end_date (:obj:`str`, optional): The end of a time interval.

        Returns:
            Trajectory: A trajectory object as a dictionary.

        Example:

            Retrieves a trajectory:

            .. doctest::
                :skipif: WLTS_EXAMPLE_URL is None

                >>> from wlts import *
                >>> service = WLTS(WLTS_EXAMPLE_URL)
                >>> tj = service.tj(latitude=-12.0, longitude=-54.0, collections='mapbiomas_amz_4_1')
                >>> ts.trajectory
                [{'class': 'Formação Florestal', 'collection': 'mapbiomas_amz_4_1', 'date': '2007'}]
        """
        invalid_parameters = set(options) - {"longitude", "latitude", "start_date", "end_date", "collections"}

        if invalid_parameters:
            raise AttributeError('invalid parameter(s): {}'.format(invalid_parameters))

        if ('latitude' not in options) or ('longitude' not in options):
            raise ValueError("Arguments latitude and longitude are mandatory.")

        if (type(options['latitude']) not in (float, int)) or (type(options['longitude']) not in (float, int)):
            raise ValueError("Arguments latitude and longitude must be numeric.")

        if (options['latitude'] < -90.0) or (options['latitude'] > 90.0):
            raise ValueError('latitude is out-of range [-90,90]!')

        if (options['longitude'] < -180.0) or (options['longitude'] > 180.0):
            raise ValueError('longitude is out-of range [-180,180]!')

        data = self._trajectory(options)

        return Trajectory(data)

    def _list_collections(self):
        """Return the list of available collections."""
        result = WLTS._get('{}/list_collections'.format(self._url))

        return result['collections']

    def _trajectory(self, params):
        """Retrieve the trajectories of collections associated with a given location in space.

        Retrieve the land use and cover trajectory associated to the
        informed location considering the given date interval and the
        collections.

        :param params: A dictionary with location and period.
        :type params: dict

        :param longitude: Longitude.
        :type longitude: float

        :param latitude: Latitude.
        :type latitude: float

        :param start_date: A string with the start date in the following format: yyyy-mm-dd.
        :type start_date: string, optional

        :param end_date: A string with the end date in the following format: yyyy-mm-dd.
        :type end_date: string, optional

        :param collections: The list of

        :returns: Trajectory.
        :rtype: list
        """
        return WLTS._get('{}/trajectory'.format(self._url), params=params)

    def _describe_collection(self, collection_id):
        """Describe a give collection.

        :param name: The collection name.
        :type name: str.

        :returns: Collection description.
        :rtype: dict
        """
        return WLTS._get('{}/describe_collection?collection_id={}'.format(self._url, collection_id))

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

    @staticmethod
    def _get(url, params=None):
        """Query the WLTS service using HTTP GET verb and return the result as a JSON document.

        :param url: The URL to query must be a valid WLTS endpoint.
        :type url: str

        :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the underlying `Requests`.
        :type params: dict

        :rtype: dict

        :raises ValueError: If the response body does not contain a valid json.
        """
        response = requests.get(url, params=params)

        response.raise_for_status()

        content_type = response.headers.get('content-type')

        if content_type.count('application/json') == 0:
            raise ValueError('HTTP response is not JSON: Content-Type: {}'.format(content_type))

        return response.json()
