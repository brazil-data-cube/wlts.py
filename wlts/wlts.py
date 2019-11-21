#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for WLTS."""
from requests import Request, Session


class wlts:
    """This class implements a Python API client wrapper for WLTS.

    See https://github.com/brazil-data-cube/wlts for more
    information on WLTS.

    :param url: The WLTS server URL.
    :type url: str
    """

    def __init__(self, url):
        """Create a WTSS client attached to the given host address (an URL)."""
        self._url = url

    def list_collections(self):
        """Return the list of available collections."""
        pass

    def trajectory(self, longitude, latitude,
                   start_date=None, end_date=None, collections=None):
        """Retrieve the trajectories of collections associated with a given location in space.

        Retrieve the land use and cover trajectory associated to the
        informed location considering the given date interval and the
        collections.

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
        pass

    def describe_collection(self, name):
        """Describe a give collection.

        :param name: The collection name.
        :type name: str.

        :returns: Collection description.
        :rtype: dict
        """
        pass

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
