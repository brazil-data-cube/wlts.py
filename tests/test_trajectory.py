#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for WLTS."""

import json
import re
from pathlib import Path

import pytest
import respx
from click.testing import CliRunner
from httpx import Response

import wlts

BASE_URL = "http://testserver/wlts"
LCCS_URL = "http://testserver/lccs"


@pytest.fixture
def wlts_objects():
    """Load json files."""
    base_path = Path(__file__).parent / "jsons"
    data = {"jsons": {}}

    for file in base_path.glob("*.json"):
        with open(file, encoding="utf-8") as f:
            data["jsons"][file.name] = json.load(f)

    return data


@pytest.fixture
def respx_mock_all(wlts_objects):
    """
    Mock jsons endpoints (WLTS + LCCS).
    """
    with respx.mock(assert_all_mocked=True) as mock:

        # Mock WLTS endpoints
        all_routes = re.compile(rf"{BASE_URL}/.*")

        def handler(request):
            url = str(request.url)
            if "/list_collections" in url:
                return Response(
                    200, json=wlts_objects["jsons"]["list_collections.json"]
                )
            elif "/describe_collection" in url:
                return Response(
                    200, json=wlts_objects["jsons"]["describe_collection.json"]
                )
            elif "/trajectory" in url:
                return Response(
                    200, json=wlts_objects["jsons"]["trajectory.json"]
                )
            else:
                return Response(404, json={"error": "Not mocked"})

        mock.get(all_routes).mock(side_effect=handler)

        # Mock LCCS endpoints
        def lccs_handler(request):
            if "/classification_systems" in str(request.url):
                return Response(
                    200,
                    json=[
                        {
                            "identifier": "1",
                            "title": "MapBiomas",
                            "version": "1.0",
                        }
                    ],
                )
            return Response(200, json=wlts_objects["jsons"]["lccs_root.json"])

        mock.get(re.compile(rf"{LCCS_URL}/.*")).mock(side_effect=lccs_handler)

        yield mock

def test_list_collection(respx_mock_all):
    client = wlts.WLTS(url=BASE_URL, lccs_url=LCCS_URL, language='pt-br')
    collections = client.collections
    assert isinstance(collections, list)
    assert "prodes_amz" in collections

def test_describe_collection(respx_mock_all):
   client = wlts.WLTS(BASE_URL, lccs_url=LCCS_URL)
   desc = client["mapbiomas-v11"]
   assert desc["collection_type"] == "Feature"


def test_trajectory(respx_mock_all):
   client = wlts.WLTS(BASE_URL, lccs_url=LCCS_URL)
   traj = client.tj(
       latitude=-12.0,
       longitude=-54.0,
       start_date="2001",
       end_date="2011",
       collections="mapbiomas-v11",
   )
   assert isinstance(traj, dict)
   assert "result" in traj
