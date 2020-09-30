#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019-2020 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""his example shows how the various text representation for services."""
from wlts import *

service = WLTS('http://brazildatacube.dpi.inpe.br/wlts/')

print(service)
print(str(service))
print(repr(service))
