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
"""Python Client Library for WLTS."""
from typing import Callable, Optional, Tuple, Union

import pandas as pd

Interval = Tuple[pd.Timestamp, pd.Timestamp]
Step = Optional[Union[pd.Timedelta, pd.DateOffset]]


def to_interval(
    df: pd.DataFrame,
    date_col: str = "date",
    step: Step = None,
) -> Optional[Interval]:
    """Derive the closed interval ``[start, end]`` covered by ``df``.

    Args:
        df: A trajectory dataframe.
        date_col: Name of the date column.
        step: Optional offset added to ``end`` to represent the period covered
            by the last observation (half-open interval). Must be positive.

    Returns:
        A ``(start, end)`` tuple of timestamps, or ``None`` when the input is
        empty or has no valid dates.
    """
    if df is None or date_col not in getattr(df, "columns", []):
        return None

    dates = pd.to_datetime(df[date_col], errors="coerce").dropna()
    if dates.empty:
        return None

    if step is not None and not isinstance(step, (pd.Timedelta, pd.DateOffset)):
        raise TypeError("step must be a pandas Timedelta or DateOffset")

    start = dates.min()
    end = dates.max() + step if step is not None else dates.max()
    return start, end


def _empty_like(a: pd.DataFrame) -> pd.DataFrame:
    """Return an empty frame preserving the columns of ``a``."""
    return pd.DataFrame(columns=getattr(a, "columns", None))


def _apply(
    a: pd.DataFrame,
    b: pd.DataFrame,
    predicate: Callable[[Interval, Interval], bool],
    step: Step = None,
) -> pd.DataFrame:
    """Return ``a`` when ``predicate`` holds for the intervals of ``a`` and ``b``."""
    interval_a = to_interval(a, step=step)
    interval_b = to_interval(b, step=step)
    if interval_a is None or interval_b is None:
        return _empty_like(a)
    if predicate(interval_a, interval_b):
        return a
    return _empty_like(a)


def before_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a before b`` (``a_e < b_s``)."""
    return _apply(a, b, lambda x, y: x[1] < y[0], step)


def after_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a after b`` (``a_s > b_e``)."""
    return _apply(a, b, lambda x, y: x[0] > y[1], step)


def equals_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a equals b`` (``a_s == b_s`` and ``a_e == b_e``)."""
    return _apply(a, b, lambda x, y: x[0] == y[0] and x[1] == y[1], step)


def meets_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a meets b`` (``a_e == b_s``)."""
    return _apply(a, b, lambda x, y: x[1] == y[0], step)


def met_by_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a met_by b`` (``a_s == b_e``)."""
    return _apply(a, b, lambda x, y: x[0] == y[1], step)


def overlaps_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a overlaps b`` (``a_s < b_s < a_e < b_e``)."""
    return _apply(a, b, lambda x, y: x[0] < y[0] < x[1] < y[1], step)


def overlapped_by_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a overlapped_by b`` (``b_s < a_s < b_e < a_e``)."""
    return _apply(a, b, lambda x, y: y[0] < x[0] < y[1] < x[1], step)


def during_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a during b`` (``b_s < a_s < a_e < b_e``)."""
    return _apply(a, b, lambda x, y: y[0] < x[0] and x[1] < y[1], step)


def contains_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a contains b`` (``a_s < b_s < b_e < a_e``)."""
    return _apply(a, b, lambda x, y: x[0] < y[0] and y[1] < x[1], step)


def starts_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a starts b`` (``a_s == b_s`` and ``a_e < b_e``)."""
    return _apply(a, b, lambda x, y: x[0] == y[0] and x[1] < y[1], step)


def started_by_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a started_by b`` (``a_s == b_s`` and ``a_e > b_e``)."""
    return _apply(a, b, lambda x, y: x[0] == y[0] and x[1] > y[1], step)


def finishes_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a finishes b`` (``b_s < a_s`` and ``a_e == b_e``)."""
    return _apply(a, b, lambda x, y: y[0] < x[0] and x[1] == y[1], step)


def finished_by_relation(a: pd.DataFrame, b: pd.DataFrame, step: Step = None) -> pd.DataFrame:
    """Represent ``a finished_by b`` (``a_s < b_s`` and ``a_e == b_e``), inverse of ``finishes``."""
    return _apply(a, b, lambda x, y: x[0] < y[0] and x[1] == y[1], step)


# TODO: add other relations (RECUR, CONVERT and EVOLVE)
"""
    before       a_e <  b_s
    after        a_s >  b_e
    meets        a_e == b_s
    met_by       a_s == b_e
    overlaps     a_s <  b_s < a_e < b_e
    overlapped_by b_s < a_s < b_e < a_e
    during       b_s <  a_s < a_e < b_e
    contains     a_s <  b_s < b_e < a_e
    starts       a_s == b_s and a_e < b_e
    started_by   a_s == b_s and a_e > b_e
    finishes     b_s <  a_s and a_e == b_e
    finished_by  a_s <  b_s and a_e == b_e
    equals       a_s == b_s and a_e == b_e
"""
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
