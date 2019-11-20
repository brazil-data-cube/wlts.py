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
    """

    def __init__(self, url):
        """Create a WTSS client attached to the given host address (an URL).
            Args:
                url (str): the WLTS server URI.
        """
        self._url = url

    def list_collections(self):
        pass

    def trajectory(self):
        pass

    def describe_collection(self):
        pass

    def list_classification_sytem(self):
        pass

    def describe_classification_sytem(self):
        pass

    @property
    def url(self):
        """Return the WLTS server instance URL."""
        return self._url

    def __repr__(self):
        """Return the string representation of a WLTS object."""
        text = '{{ "url": "{}" }}'.format(self.url)
        return text

    def __str__(self):
        """Return the string representation of a WLTS object."""
        return '<WLTS [{}]>'.format(self.url)
