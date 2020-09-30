#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""A class that represents a collection in WTSS."""


class Collections(dict):
    """A class that describes a collection in WTSS.

    .. note::
        For more information about collection definition, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, service, metadata=None):
        """Create a collection object associated to a WLTS client.

        Args:
            service (wlts.WLTS): The client to be used by the collection object.
            metadata (dict): The collection metadata.
        """
        #: WLTS: The associated WLTS client to be used by the collection object.
        self._service = service

        super(Collections, self).__init__(metadata or {})

        @property
        def collection_type(self):
            """Return the coverage dimensions metadata."""
            return self['collection_type']

        @property
        def description(self):
            """Return the coverage dimensions metadata."""
            return self['description']

        @property
        def detail(self):
            """Return the coverage dimensions metadata."""
            return self['detail']
        @property
        def name(self):
            """Return the coverage dimensions metadata."""
            return self['name']

        @property
        def period(self):
            """Return the coverage dimensions metadata."""
            return self['period']

        @property
        def resolution_unit(self):
            """Return the coverage dimensions metadata."""
            return self['resolution_unit']

        @property
        def spatial_extent(self):
            """Return the coverage dimensions metadata."""
            return self['spatial_extent']

        def __str__(self):
            """Return the string representation of the Collection object."""
            return super().__str__()

        def __repr__(self):
            """Return the Collection object representation."""
            wlts_repr = repr(self._service)

            text = f'Collection(service={wlts_repr}, metadata={super().__repr__()}'

            return text

