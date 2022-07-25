#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python API client wrapper for WLTS."""
from .utils import Utils


class Trajectories(dict):
    """A class that represents a multiples trajectories in WLTS.

    .. note::
        For more information about trajectory definition, please, refer to
        `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, data):
        """Create a Trajectories object.

        Args:
            data: The trajectories.
        """
        super(Trajectories, self).__init__(data or {})

    def _repr_html_(self):
        """HTML repr."""
        return Utils.render_html('trajectory.html', trajectories=self)

    def df(self, **options):
        """Plot trajectory as dataframe."""
        import pandas as pd

        trjs_df = [trj.df() for trj in self['trajectories']]

        return pd.concat(trjs_df, axis=0).reset_index(drop=True)

