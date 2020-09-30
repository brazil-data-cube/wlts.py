#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command line interface for the STAC client."""

import json
from pprint import pprint

import click

from .wlts import wlts


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialization of Config decorator."""
        self.url = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', type=click.STRING, default='http://localhost',
              help='The WLTS server address (an URL).')
@pass_config
def cli(config, url):
    """WLTS on command line."""
    config.url = url


@cli.command()
@pass_config
def collections(config):
    """Return the list of available collections in the service provider."""
    service = wlts(config.url)

    retval = service.list_collections()

    pprint(retval)


@cli.command()
@click.option('--geoloc', nargs=2, type=click.FLOAT,
              help='''The x and y coordinates of the query location
                      (required if --ifile is omitted or if x and y
                       arguments are omitted).''',
              required=False)
@click.option('--ifile', type=click.File('r'),
              help='A JSON input file with all query parameters (required if --geoloc is omitted).',
              required=False)
@click.argument('x', type=click.FLOAT, required=False)
@click.argument('y', type=click.FLOAT, required=False)
@pass_config
def trajectory(config, geoloc, ifile, x, y):
    """Return the trajectory associated to the location."""
    query = {}

    if ifile is not None:
        query = json.load(ifile)
    elif geoloc:
        query.update(dict(
            longitude=geoloc[1],
            latitude=geoloc[0]
        ))
    else:
        query.update(dict(
            longitude=y,
            latitude=x
        ))


    service = wlts(config.url)

    retval = service.trajectory(query)

    pprint(retval)


