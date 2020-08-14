#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for WLTS."""
import requests


class wlts:
    """This class implements a Python API client wrapper for WLTS.

    See https://github.com/brazil-data-cube/wlts for more
    information on WLTS.

    :param url: The WLTS server URL.
    :type url: str
    """

    def __init__(self, url):
        """Create a WTSS client attached to the given host address (an URL)."""
        self._url = url if url[-1] != '/' else url[0:-1]


    def list_collections(self):
        """Return the list of available collections."""
        return self._get('{}/list_collections'.format(self._url))


    def trajectory(self, params):
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
        return self._get('{}/trajectory'.format(self._url), params=params)


    def describe_collection(self, collection_id):
        """Describe a give collection.

        :param name: The collection name.
        :type name: str.

        :returns: Collection description.
        :rtype: dict
        """
        return self._get('{}/describe_collection?collection_id={}'.format(self._url, collection_id))


    def list_classification_sytem(self):
        """Return the list of available land use and land cover classification system."""
        pass


    def describe_classification_sytem(self):
        """List all classes of a land use and cover classification system."""
        pass


    @property
    def url(self):
        """Return the WLTS server instance URL."""
        return self._url


    def __repr__(self):
        """Return the string representation of a WLTS object."""
        text = 'wlts("{}")'.format(self.url)
        return text


    def __str__(self):
        """Return the string representation of a WLTS object."""
        return '<WLTS [{}]>'.format(self.url)


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
