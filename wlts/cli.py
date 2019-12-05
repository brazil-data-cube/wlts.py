#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Command line interface for the STAC client."""

from pprint import pprint

import click

from .wlts import wlts


@click.group()
def cli():
    """WLTS on command line."""
    pass


@click.command()
@click.option('--url', default='http://localhost', help='The WLTS server address (an URL).')
def collections(url):
    """Return the list of available collections in the service provider."""
    service = wlts(url)

    retval = service.list_collections()

    pprint(retval)


cli.add_command(collections)