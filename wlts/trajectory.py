#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2020 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for WLTS."""


class Trajectory(dict):
    """A class that represents a collection in WLTS.

    .. note::
        For more information about time series definition, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, data):
        """Create a Trajectory object.

        Args:
            trajectory: The result of trajectory.
        """
        super(Trajectory, self).__init__(data or {})

    @property
    def trajectory(self, as_date=False, fmt=''):
        """Return the timeline associated to the time series."""
        return self['result']['trajectory']

    @property
    def query(self, as_date=False, fmt=''):
        """Return the timeline associated to the time series."""
        return self['query']

    def df(self, **options):
        """Plot trajectory as dataframe."""
        try:
            import pandas as pd
        except:
            raise ImportError('You should install Pandas')

        return pd.DataFrame.from_dict(self.trajectory)
