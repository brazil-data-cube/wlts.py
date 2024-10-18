#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2022 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""This example shows how to retrieve this list of collections."""

from wlts import WLTS

# You should create a wlts object attached to a given service
# Specify the URL of the WLTS instance to be used
service = WLTS('https://data.inpe.br/bdc/wlts/v1/')

# Returns the list of collections available on the service
print(service.collections)
