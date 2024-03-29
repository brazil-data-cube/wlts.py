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
"""A class that represents a Collection in WLTS."""
from .utils import Utils


class Collections(dict):
    """A class that describes a collection in WLTS.

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
        """Return the type of the collection."""
        return self['collection_type']

    @property
    def description(self):
        """Return the description of the collection."""
        return self['description']

    @property
    def detail(self):
        """Return the detail of the collection."""
        return self['detail']

    @property
    def name(self):
        """Return the name of the collection."""
        return self['name']

    @property
    def title(self):
        """Return the title of the collection."""
        return self['title']

    @property
    def period(self):
        """Return the period of the collection."""
        return self['period']

    @property
    def temporal_resolution(self):
        """Return the temporal resolution of the collection."""
        return self['temporal_resolution']

    @property
    def spatial_extent(self):
        """Return the spatial extent of the collection."""
        return self['spatial_extent']

    @property
    def classification_system(self):
        """Return the classification system of the collection."""
        return self['classification_system']

    def __str__(self):
        """Return the string representation of the Collection object."""
        return super().__str__()

    def __repr__(self):
        """Return the Collection object representation."""
        wlts_repr = repr(self._service)

        text = f'Collection(service={wlts_repr}, metadata={super().__repr__()}'

        return text

    def _repr_html_(self):
        """HTML repr."""
        return Utils.render_html('collection.html', collection=self)
