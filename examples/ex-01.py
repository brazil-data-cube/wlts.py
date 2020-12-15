#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019-2020 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""


from wlts import WLTS

# You should create a WLTS object attached to a given service
# (Specify the URL of the WLTS instance to be used ):
service = WLTS('http://brazildatacube.dpi.inpe.br/wlts/')

print(repr(service))
print(str(service))

# Returns the list of collections available on the service
print(service.collections)

# Return the metadata of a specific collection
# The collection name may not be same.
# Make sure the collection is available in service, using the previous operation (service.collection)
print(service['deter_amz_legal'])

# Example of trajectory operation
# The collection name may not be same.
# Make sure the collection is available in service, using the previous operation (service.collection)
tj = service.tj(latitude=-12.0, longitude=-54.0, collections='mapbiomas5_amazonia')

print(tj.trajectory)
