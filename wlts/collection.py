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
from typing import Any, Dict, Union

from .utils import Utils


class Collections(dict):
    """A class that describes a collection in WLTS.

    For more information about collection definition, refer to
    `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, service: Any, metadata: Dict[str, Any] = None) -> None:
        """Create a collection object associated to a WLTS client.

        Args:
            service (wlts.WLTS): The client to be used by the collection object.
            metadata (Dict[str, Any]): The collection metadata.
        """
        self._service = service
        super().__init__(metadata or {})

    @property
    def collection_type(self) -> str:
        """Return the type of the collection."""
        return self['collection_type']

    @property
    def description(self) -> str:
        """Return the description of the collection."""
        return self['description']

    @property
    def detail(self) -> str:
        """Return the detail of the collection."""
        return self['detail']

    @property
    def name(self) -> str:
        """Return the name of the collection."""
        return self['name']

    @property
    def title(self) -> str:
        """Return the title of the collection."""
        return self['title']

    @property
    def period(self) -> Union[str, None]:
        """Return the period of the collection."""
        return self.get('period')

    @property
    def temporal_resolution(self) -> str:
        """Return the temporal resolution of the collection."""
        return self['temporal_resolution']

    @property
    def spatial_extent(self) -> Dict[str, Any]:
        """Return the spatial extent of the collection."""
        return self['spatial_extent']

    @property
    def classification_system(self) -> Dict[str, Any]:
        """Return the classification system of the collection."""
        return self['classification_system']

    def __str__(self) -> str:
        """Return the string representation of the Collection object."""
        return super().__str__()

    def __repr__(self) -> str:
        """Return the Collection object representation."""
        wlts_repr = repr(self._service)
        return f'Collection(service={wlts_repr}, metadata={super().__repr__()})'

    def _repr_html_(self) -> str:
        """HTML representation for IPython rich display."""
        return Utils.render_html('collection.html', collection=self)
