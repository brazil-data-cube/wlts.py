#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2020-2021 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python Client Library for the Web Land Trajectory Service."""

from .version import __version__
from .wlts import WLTS

__all__ = ('__version__',
           'WLTS',)
