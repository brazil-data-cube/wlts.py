#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2023 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""

from wlts import WLTS

# You should create a WLTS object attached to a given service
# (Specify the URL of the WLTS instance to be used ):
service = WLTS('https://data.inpe.br/bdc/wlts/v1/')

print(repr(service))
print(str(service))

# Returns the list of collections available on the service
print(service.collections)

# Return the metadata of a specific collection
# The collection name may not be same.
# Make sure the collection is available in service, using the previous operation (service.collection)
print(service['deter_amazonia_legal'])

# Example of trajectory operation
# The collection name may not be same.
# Make sure the collection is available in service, using the previous operation (service.collection)
tj = service.tj(
    latitude=-12.0,
    longitude=-54.0,
    collections='mapbiomas-v9'
)
