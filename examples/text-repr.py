#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2022 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""This example shows how the various text representation for services."""

from wlts import *

service = WLTS('https://data.inpe.br/bdc/wlts/v1/')

print(service)
print(str(service))
print(repr(service))
print(service._repr_html_())

