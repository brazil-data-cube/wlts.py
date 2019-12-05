#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for WLTS' trajectory operation."""

import os

from wlts import wlts

url =  os.environ.get('WLTS_SERVER_URL', 'http://localhost')


def test_creation():
    service = wlts(url)

    assert url.count(service.url) == 1


def test_repr():
    service = wlts(url)

    assert repr(service) == 'wlts("{}")'.format(url)


def test_str():
    service = wlts(url)

    assert str(service) == '<WLTS [{}]>'.format(url)


def test_collections():
    service = wlts(url)

    retval = service.list_collections()

    #assert 'feature_collection' in retval


def test_trajectory():
    service = wlts(url)

    query = dict(
        latitude=-64.285,
        longitude=-8.706
    )

    retval = service.trajectory(query)

    assert 'query' in retval
