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
"""A class that represents Trajectories in WLTS."""
from typing import Any, Dict

import pandas as pd

from .utils import Utils


class Trajectories(dict):
    """A class that represents multiple trajectories in WLTS.

    For more information about trajectory definition, refer to
    `WLTS specification <https://github.com/brazil-data-cube/wlts-spec>`_.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        """Create a Trajectories object.

        Args:
            data (Dict[str, Any]): The trajectories data.
        """
        super().__init__(data or {})

    def _repr_html_(self) -> str:
        """Display the trajectories as HTML for IPython rich display."""
        return Utils.render_html('trajectory.html', trajectories=self)

    def df(self, **options: Any) -> pd.DataFrame:
        """Return the dataframe representation of the Trajectories object."""
        trjs_df = [trj.df() for trj in self['trajectories']]
        return pd.concat(trjs_df, axis=0).reset_index(drop=True)