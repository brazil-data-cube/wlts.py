#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command line interface for the WLTS client."""

import click

from .wlts import WLTS


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialization of Config decorator."""
        self.url = None
        self.service = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', type=click.STRING, default='https://brazildatacube.dpi.inpe.br/wlts/',
              help='The WLTS server address (an URL).')
@click.option('--access-token', default=None, help='Personal Access Token of the BDC Auth')
@click.version_option()
@pass_config
def cli(config, url, access_token):
    """WLTS on command line."""
    config.url = url
    config.service = WLTS(url, access_token=access_token)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def list_collections(config: Config, verbose):
    """Return the list of available collections in the service provider."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the list of available coverages... ',
                    bold=False, fg='black')
        for collection in config.service.collections:
            click.secho(f'\t\t- {collection}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        for cv in config.service.collections:
            click.secho(f'{cv}', bold=True, fg='green')


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('-c', '--collection', required=True, type=str,
              help='The collection name')
@pass_config
def describe(config: Config, verbose, collection):
    """Retrieve the coverage metadata."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the collection metadata... ',
                    bold=False, fg='black')

    cv = config.service[collection]

    click.secho(f'\t- {cv}', bold=True, fg='green')

    if verbose:
        click.secho('\tFinished!', bold=False, fg='black')


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@click.option('-a', '--collections', required=False, type=str,
              help='Collections list (items separated by comma)')
@click.option('--latitude', required=True, type=float,
              help='Latitude in EPSG:4326')
@click.option('--longitude', required=True, type=float,
              help='Longitude in EPSG:4326')
@click.option('--start-date', required=False, type=str,
              help='Start date')
@click.option('--end-date', required=False, type=str,
              help='End date')
@click.option('--start-date', required=False, type=str,
              help='Start date')
@click.option('--end-date', required=False, type=str,
              help='End date')
@pass_config
def trajectory(config: Config, verbose, collections, start_date, end_date, latitude, longitude):
    """Return the trajectory associated to the location."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving trajectory... ',
                    bold=False, fg='black')

    retval = config.service.tj(latitude=latitude, longitude=longitude,
                               collections=collections, start_date=start_date, end_date=end_date)

    click.secho(f'\ttrajectory: {retval.trajectory}')

    if verbose:
        click.secho('\tFinished!', bold=False, fg='black')
