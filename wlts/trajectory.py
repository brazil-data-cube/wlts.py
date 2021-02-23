#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2020-2021 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for WLTS."""


class Trajectory(dict):
    """A class that represents a collection in WLTS.

    .. note::
        For more information about trajectory definition, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, data):
        """Create a Trajectory object.

        Args:
            data: The result of trajectory.
        """
        super(Trajectory, self).__init__(data or {})

    @property
    def trajectory(self, as_date=False, fmt=''):
        """Return the trajectory associated with a location in space."""
        return {'latitude': self['query']['latitude'], 'longitude': self['query']['longitude'], 'trajectory': self['result']['trajectory']}

    @property
    def query(self, as_date=False, fmt=''):
        """Return the query."""
        return self['query']

    def df(self, **options):
        """Plot trajectory as dataframe."""
        try:
            import pandas as pd
        except:
            raise ImportError('You should install Pandas')

        return pd.DataFrame(self.trajectory['trajectory'])

    def geodf(self, **options):
        """Plot trajectory as geodataframe."""
        if not all(['geom' in i for i in self.trajectory['trajectory']]):
            raise RuntimeError("Geometry field not exist! Verify if you pass geometry=True in service.trj!")
        try:
            import geopandas as gpd
            from shapely.geometry import shape
        except:
            raise ImportError('You should install GeoPandas, Shapely and Descartes!')

        gdf = gpd.GeoDataFrame(self.trajectory['trajectory'])
        
        gdf["geom"] = gdf.apply(lambda x: shape(x["geom"]), axis=1)

        gdf.set_geometry("geom", inplace=True)
        gdf.set_crs("EPSG:4326", inplace=True)

        return gdf
