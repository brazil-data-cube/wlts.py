#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""

from wlts import WLTS

# Specify the URL of the WLTS instance to be used
service = WLTS('https://brazildatacube.dpi.inpe.br/wlts/')

# Get collection metadata
print(service['prodes_amazonia_legal'])
