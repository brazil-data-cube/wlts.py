#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019-2020 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""

from wlts import WLTS

# Change to the WLTS URL you want to use.
service = WLTS('http://brazildatacube.dpi.inpe.br/wlts/')

# Get collection metadata
print(service['prodes_amz_legal'])
