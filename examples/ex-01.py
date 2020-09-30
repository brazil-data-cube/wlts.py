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

print(repr(service))
print(str(service))

# Returns the list of collections available on the service
print(service.collections)

# Get Service metadata
print(service['deter_amz_legal'])

# Example of trajectory operation
tj = service.tj(latitude=-12.0, longitude=-54.0, collections='mapbiomas_amz_4_1')

print(tj.trajectory)
