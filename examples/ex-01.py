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

url =  os.environ.get('WLTS_SERVER_URL', 'http://0.0.0.0:5000/wlts/')

service = wlts(url)

# Retorna a lista de collections disponiveis no servico
print(service.list_collections())

# Retorna os metadados do prodes collection
print(service.describe_collection(name="prodes"))

# Exemplos da operacao de trajetoria

# Sao informados os parametros obrigatorios de latitude e longitude
trj_um = service.trajectory(dict(latitude=-64.285, longitude=-8.706))


for trj in trj_um['result']['trajectory']:
  print("Collection: {}, Class: {}, Date: {}".format(trj['collection'], trj['class'], trj['date']))

# Retorna a trajetoria apenas do terraclass collections
trj_tc = service.trajectory(dict(latitude=-64.285, longitude=-8.706, collections='terraclass'))

for trj in trj_tc['result']['trajectory']:
  print("Collection: {}, Class: {}, Date: {}".format(trj['collection'], trj['class'], trj['date']))
