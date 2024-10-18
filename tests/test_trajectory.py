#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for WLTS."""

import json
import os
import re
from pathlib import Path

import pytest
from click.testing import CliRunner
from pkg_resources import resource_filename, resource_string

import wlts
from wlts.cli import Config

url = os.environ.get('WLTS_SERVER_URL', 'http://localhost:5000/wlts')
match_url = re.compile(url)


@pytest.fixture
def requests_mock(requests_mock):
    requests_mock.get(re.compile('https://geojson.org/'), real_http=True)
    yield requests_mock


@pytest.fixture(scope='session')
def wlts_objects():
    directory = resource_filename(__name__, 'jsons/')
    files = dict()
    for path in Path(directory).rglob('*.json'):
        path = str(path)
        s = path.split('/')

        file_path = '/'.join(s[-2:])

        print(file_path)

        file = json.loads(resource_string(__name__, file_path).decode('utf-8'))
        if s[-2] in files:
            files[s[-2]][s[-1]] = file
        else:
            files[s[-2]] = {s[-1]: file}

    return files


@pytest.fixture(scope='module')
def runner():
    return CliRunner()


@pytest.fixture
def config_obj():
    config = Config()
    config.url = url
    config.service = wlts.WLTS(url)

    return config


class TestWLTS:

    def test_wlts(self):
        service = wlts.WLTS(url)
        assert service.url == url
        assert str(service) == f'WLTS:\n\tURL: {url}'
        assert repr(service) == f'wlts(url="{url}")'

    def test_list_collection(self, wlts_objects, requests_mock):
        for k in wlts_objects:
            s = wlts.WLTS(url)
            requests_mock.get(match_url, json=wlts_objects[k]['list_collections.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            response = s.collections

            assert type(response) == list
            assert response == ["prodes_amz", "prodes_cerrado", "deter_amz",
                                "deter_cerrado", "mapbiomas_4_1_amz"]

    def test_describe_collection(self, wlts_objects, requests_mock):
        for k in wlts_objects:
            s = wlts.WLTS(url)

            requests_mock.get(match_url, json=wlts_objects[k]['describe_collection.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            collection = s['prodes_cerrado']

            assert collection == wlts_objects[k]['describe_collection.json']
            assert collection['collection_type']
            assert collection['description']
            assert collection['detail']
            assert collection['name']
            assert collection['period']
            assert collection['resolution_unit']
            assert collection['spatial_extent']

    def test_trajectory(self, wlts_objects, requests_mock):
        for k in wlts_objects:
            s = wlts.WLTS(url)

            requests_mock.get(match_url, json=wlts_objects[k]['trajectory.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            trajectory = s.tj(latitude=-12.0, longitude=-54.0, start_date='2001', end_date='2011',
                              collections='mapbiomas5_amazonia')

            assert 'query' in trajectory
            assert 'result' in trajectory
            assert trajectory['query']['latitude']
            assert trajectory['query']['longitude']
            assert 'trajectory' in trajectory['result']


class TestCli:
    def test_collection(self, wlts_objects, requests_mock, runner, config_obj):
        for k in wlts_objects:
            requests_mock.get(match_url, json=wlts_objects[k]['list_collections.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            result = runner.invoke(wlts.cli.list_collections, obj=config_obj)

            assert result.exit_code == 0
            assert 'prodes_amz' in result.output

    def test_describe(self, wlts_objects, requests_mock, runner, config_obj):
        for k in wlts_objects:
            requests_mock.get(match_url, json=wlts_objects[k]['describe_collection.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            result = runner.invoke(wlts.cli.describe, ['--collection', 'prodes_cerrado'], obj=config_obj)

            assert result.exit_code == 0
            assert 'collection_type' in result.output
            assert 'description' in result.output
            assert 'detail' in result.output
            assert 'name' in result.output

    def test_trajectory(self, wlts_objects, requests_mock, runner, config_obj):
        for k in wlts_objects:
            requests_mock.get(match_url, json=wlts_objects[k]['trajectory.json'],
                              status_code=200,
                              headers={'content-type': 'application/json'})

            result = runner.invoke(wlts.cli.trajectory, ['--collections', 'mapbiomas5_amazonia',
                                                         '--latitude', '-12.0',
                                                         '--longitude', '-54.0',
                                                         '--start-date', '2001',
                                                         '--end-date', '2011'
                                                         ], obj=config_obj)

            assert result.exit_code == 0
            assert 'Processing trajectory request...' in result.output


if __name__ == '__main__':
    import pytest

    pytest.main(['--color=auto', '--no-cov'])
