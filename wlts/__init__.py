#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python Client Library for the Web Land Trajectory Service."""

from . import cli
from .version import __version__
from .wlts import WLTS

__all__ = ('__version__',
           'WLTS',)
