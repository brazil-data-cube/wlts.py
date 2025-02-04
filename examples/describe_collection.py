#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2022 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""This example shows how to retrieve the collection metadata."""

from wlts import WLTS

# Specify the URL of the WLTS instance to be used
service = WLTS('https://data.inpe.br/bdc/wlts/v1')

# Get collection metadata
print(service['prodes_amazonia_legal'])
