#
# This file is part of Python Client Library for the WLTS.
# Copyright (C) 2025 INPE.
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
"""Python Client Library for WLTS.

This module introduces a class named ``WLTS`` that can be used to retrieve
trajectories for a given location.
"""

import pandas as pd


def before_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """The function represets a < b."""
    if (a["date"].max() < b["date"].min()):
        return a
    return pd.DataFrame(columns=a.columns)


def after_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """The function represets a > b."""
    if (a["date"].min() > b["date"].max()):
        return a
    return pd.DataFrame(columns=a.columns)


def equals_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """The function represets a == b."""
    if set(a["date"]) & set(b["date"]):
        return a[a["date"].isin(b["date"])]
    return pd.DataFrame(columns=a.columns)

def meets_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a meets b  (a == b - 1)."""
    if any(a["date"].isin(b["date"] - pd.Timedelta(days=1))):
        return a
    return pd.DataFrame(columns=a.columns)


def met_by_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a met_by b  (a == b + 1)."""
    if any(a["date"].isin(b["date"] + pd.Timedelta(days=1))):
        return a
    return pd.DataFrame(columns=a.columns)


def overlaps_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a overlaps b  (a <= b & a + 1 >= b)."""
    if any((a["date"].min() <= b["date"]) & ((a["date"].max() + pd.Timedelta(days=1)) >= b["date"])):
        return a
    return pd.DataFrame(columns=a.columns)


def overlapped_by_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a overlapped_by b  (a <= b & a + 1 <= b)."""
    if any((a["date"].min() <= b["date"]) & ((a["date"].max() + pd.Timedelta(days=1)) <= b["date"])):
        return a
    return pd.DataFrame(columns=a.columns)


def during_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a during b  (a >= b & a + 1 <= b)."""
    if (a["date"].min() >= b["date"].min()) and ((a["date"].max() + pd.Timedelta(days=1)) <= b["date"].max()):
        return a
    return pd.DataFrame(columns=a.columns)


def contains_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a contains b  (a <= b & a + 1 >= b)."""
    if (a["date"].min() <= b["date"].min()) and ((a["date"].max() + pd.Timedelta(days=1)) >= b["date"].max()):
        return a
    return pd.DataFrame(columns=a.columns)


def starts_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a starts b  (a == b & a + 1 <= b)."""
    if (a["date"].min() == b["date"].min()) and ((a["date"].max() + pd.Timedelta(days=1)) <= b["date"].max()):
        return a
    return pd.DataFrame(columns=a.columns)


def started_by_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a started_by b  (a == b & a + 1 >= b)."""
    if (a["date"].min() == b["date"].min()) and ((a["date"].max() + pd.Timedelta(days=1)) >= b["date"].max()):
        return a
    return pd.DataFrame(columns=a.columns)


def finishes_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a finishes b  (a <= b & a + 1 == b)."""
    if (a["date"].min() <= b["date"].min()) and ((a["date"].max() + pd.Timedelta(days=1)) == b["date"].max()):
        return a
    return pd.DataFrame(columns=a.columns)


def finished_by_relation(a: pd.DataFrame, b: pd.DataFrame) -> pd.DataFrame:
    """Represents a finished_by b  (a <= b & a + 1 == b)."""
    if (a["date"].min() <= b["date"].min()) and ((a["date"].max() + pd.Timedelta(days=1)) == b["date"].max()):
        return a
    return pd.DataFrame(columns=a.columns)



# TODO: add other relations (RECUR, CONVERT and EVOLVE)
ALLEN_RELATIONS = {
    "before": before_relation,
    "after": after_relation,
    "equals": equals_relation,
    "meets": meets_relation,
    "met_by": met_by_relation,
    "overlaps": overlaps_relation,
    "overlapped_by": overlapped_by_relation,
    "during": during_relation,
    "contains": contains_relation,
    "starts": starts_relation,
    "started_by": started_by_relation,
    "finishes": finishes_relation,
    "finished_by": finished_by_relation,
}


