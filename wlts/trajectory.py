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
"""A class that represents Trajectory in WLTS."""
from typing import Any, Dict, List

import geopandas as gpd
import pandas as pd
from shapely.geometry import shape

from .utils import Utils


class Trajectory(dict):
    """A class that represents a trajectory in WLTS.

    .. note::
        For more information about trajectory definition, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """Create a Trajectory object.

        Args:
            data: The result of trajectory.
        """
        super(Trajectory, self).__init__(data or {})

    @property
    def trajectory(self, as_date=False, index: int = 1, fmt="") -> List[Dict[str, Any]]:
        """Return the trajectory associated with a location in space."""
        return self["result"]["trajectory"]

    @property
    def query(self, as_date=False, fmt="") -> Dict[str, Any]:
        """Return the query."""
        return self["query"]

    def df(self, **options) -> pd.DataFrame:
        """Return the dataframe representation of the Trajectory object."""
        return pd.DataFrame(self.trajectory)

    def geodf(self, **options) -> gpd.GeoDataFrame:
        """Return the geodataframe representation of the Trajectory object."""
        if not all(["geom" in i for i in self.trajectory]):
            raise RuntimeError(
                "Geometry field not exist! Verify if you pass geometry=True in service.trj!"
            )
        gdf = gpd.GeoDataFrame(self.trajectory)

        gdf["geom"] = gdf.apply(lambda x: shape(x["geom"]), axis=1)

        gdf.set_geometry("geom", inplace=True)
        gdf.set_crs("EPSG:4326", inplace=True)

        return gdf

    def _repr_html_(self) -> str:
        """Display the trajectory as HTML.

        This integrates a rich display in IPython.
        """
        return Utils.render_html("trajectory-item.html", tj=self)
