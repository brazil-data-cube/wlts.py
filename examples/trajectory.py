#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019-2020 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""

from wlts import WLTS

# Specify the URL of the WLTS instance to be used
service = WLTS('http://brazildatacube.dpi.inpe.br/wlts/')

# Example of trajectory operation
tj = service.tj(latitude=-12.0, longitude=-54.0)

print(tj.trajectory)

# The collection name may not be same.
# Make sure the collection is available in service
tj_two = service.tj(latitude=-12.0, longitude=-54.0, collections='mapbiomas5_amazonia')

print(tj_two.trajectory)
