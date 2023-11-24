#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2023 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""This example shows how to retrieve a trajectory with harmonize classes."""
import os

from lccs import LCCS

from wlts import WLTS

# Define Services

lccs_url = os.environ.get('LCCS_SERVER_URL', 'https://brazildatacube.dpi.inpe.br/lccs/')
wlts_url = os.environ.get('LCCS_SERVER_URL', 'https://brazildatacube.dpi.inpe.br/wlts/')

service_wlts = WLTS(url=wlts_url, lccs_url=lccs_url, access_token='change-me')
service_lccs = LCCS(url=lccs_url)

# Find the classification system of collections
collection_1 = service_wlts['terraclass_amazonia'].classification_system
collection_2 = service_wlts['prodes_amazonia_legal'].classification_system

# Show available classification system mappings
mp = service_lccs.available_mappings(
	system_source=f'{collection_1["name"]}-{collection_1["version"]}'
)

print(mp)

# Get a trajectory for a target system
tj = service_wlts.tj(
	latitude=-6.282295,
	longitude=-52.53655,
	collections='terraclass_amazonia,prodes_amazonia_legal',
	target_system=mp[0].identifier
)
print(tj.df())