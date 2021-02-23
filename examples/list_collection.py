#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2020-2021 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""

from wlts import WLTS

# You should create a wlts object attached to a given service
# Specify the URL of the WLTS instance to be used
service = WLTS('https://brazildatacube.dpi.inpe.br/wlts/')

# Returns the list of collections available on the service
print(service.collections)
