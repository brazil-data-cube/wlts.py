#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for WLTS' trajectory operation."""

from wlts import wlts

url = 'http://localhost:5000'

def test_uri():
    service = wlts(url)

    assert service.url == url


def test_repr():
    service = wlts(url)

    assert repr(service) == 'wlts("{}")'.format(url)


def test_str():
    service = wlts(url)

    assert str(service) == '<WLTS [{}]>'.format(url)
