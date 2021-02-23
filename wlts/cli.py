#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command line interface for the WLTS client."""

import json
from pprint import pprint

import click

from .wlts import WLTS


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialization of Config decorator."""
        self.url = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', type=click.STRING, default='https://brazildatacube.dpi.inpe.br/wlts/',
              help='The WLTS server address (an URL).')
@pass_config
def cli(config, url):
    """WLTS on command line."""
    config.url = url


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def collections(config, verbose):
    """Return the list of available collections in the service provider."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the list of available coverages... ',
                    bold=False, fg='black')

    service = WLTS(config.url)

    retval = service.collections

    pprint(retval)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('-c', '--collection', required=True, type=str,
              help='Collection name')
@pass_config
def describe(config, verbose, collection):
    """Retrieve the coverage metadata."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the collection metadata... ',
                    bold=False, fg='black')

    service = WLTS(config.url)

    cv = service[collection]

    click.secho(f'\t- {cv}', bold=True, fg='green')

    if verbose:
        click.secho('\tFinished!', bold=False, fg='black')


@cli.command()
@click.option('--geoloc', nargs=2, type=click.FLOAT,
              help='''The x and y coordinates of the query location
                      (required if --ifile is omitted or if x and y
                       arguments are omitted).''',
              required=False)
@click.option('--ifile', type=click.File('r'),
              help='A JSON input file with all query parameters (required if --geoloc is omitted).',
              required=False)
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.argument('x', type=click.FLOAT, required=False)
@click.argument('y', type=click.FLOAT, required=False)
@pass_config
def trajectory(config, verbose, geoloc, ifile, x, y):
    """Return the trajectory associated to the location."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving trajectory... ',
                    bold=False, fg='black')
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

    service = WLTS(config.url)

    retval = service.tj(**query)

    pprint(retval.trajectory)
