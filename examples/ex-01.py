#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Samples."""

import os

from wlts import wlts

# Change to the WLTS URL you want to use.
url =  os.environ.get('WLTS_SERVER_URL', 'http://0.0.0.0:5000/wlts/')

service = wlts(url)

# Returns the list of collections available on the service
print(service.list_collections())

# Example of trajectory operation

# Inform the mandatory parameters (latitude and longitude)
trj_um = service.trajectory(dict(latitude=-8.706, longitude=-64.285))

for trj in trj_um['result']['trajectory']:
  print("Collection: {}, Class: {}, Date: {}".format(trj['collection'], trj['class'], trj['date']))
