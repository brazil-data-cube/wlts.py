#
# This file is part of Python Client Library for the WLTS.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#

"""Command line interface for the WLTS client."""
from time import time

import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.tree import Tree

from .wlts import WLTS


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialization of Config decorator."""
        self.url = None
        self.service = None
        self.lccs_url = None


pass_config = click.make_pass_decorator(Config, ensure=True)

console = Console()


@click.group()
@click.option(
    "--url",
    type=click.STRING,
    default="https://data.inpe.br/bdc/wlts/v1/",
    help="The WLTS server address (an URL).",
)
@click.option(
    "--lccs-url",
    type=click.STRING,
    default="https://data.inpe.br/bdc/lccs/v1",
    help="The LCCS-WS address (an URL).",
)
@click.option(
    "--access-token", default=None, help="Personal Access Token of the BDC Auth"
)
@click.version_option()
@pass_config
def cli(config, url, lccs_url, access_token):
    """WLTS on command line."""
    config.url = url
    config.service = WLTS(url, lccs_url=lccs_url, access_token=access_token)


@cli.command()
@click.option("-v", "--verbose", is_flag=True, default=False)
@pass_config
def list_collections(config: Config, verbose):
    """Return the list of available collections in the service provider."""
    if verbose:
        console.print(f"[bold black]Server: [green]{config.url}[/green]", style="bold")
        console.print(
            "[black]\tRetrieving the list of available collections...[/black]"
        )

        table = Table(
            title="Available Collections", show_header=True, header_style="bold magenta"
        )
        table.add_column("Collection Name", style="green", no_wrap=True)
        table.add_column("Collection Title", style="green", no_wrap=True)

        for collection in config.service.collections:
            describe_collection = config.service[collection]
            table.add_row(collection, describe_collection["title"])

        console.print(table)
        console.print("[black]\tFinished![/black]")

    else:
        for collection in config.service.collections:
            console.print(f"[green]{collection}[/green]", style="bold")


@cli.command()
@click.option("-v", "--verbose", is_flag=True, default=False)
@click.option("-c", "--collection", required=True, type=str, help="The collection name")
@pass_config
def describe(config: Config, verbose, collection):
    """Retrieve the collection metadata."""
    cv = config.service[collection]

    if verbose:
        console.print(f"[bold black]Server: [green]{config.url}[/green]", style="bold")
        console.print("[black]\tRetrieving the collection metadata...[/black]")

        tree = Tree(cv["title"], guide_style="bold cyan")


        tree.add(f"[bold green]ID[/bold green]: {cv['classification_system']['id']}")
        tree.add(f"[bold green]Name[/bold green]: {cv['classification_system']['name']}")
        tree.add(f"[bold green]Title[/bold green]: {cv['classification_system']['title']}")
        tree.add(f"[bold green]Version[/bold green]: {cv['classification_system']['version']}")
        tree.add(f"[bold green]Type[/bold green]: {cv['classification_system']['type']}")

        table = Table(title="Overview", expand=True)
        table.add_column("Key", justify="right", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        table.add_row("Collection Type", cv["collection_type"])
        table.add_row("Description", cv["description"])
        table.add_row("Period", f"{cv['period']['start_date']} a {cv['period']['end_date']}")
        table.add_row("Spatial Extent",
                      f"Xmin: {cv['spatial_extent']['xmin']}, Xmax: {cv['spatial_extent']['xmax']}, Ymin: {cv['spatial_extent']['ymin']}, Ymax: {cv['spatial_extent']['ymax']}")
        table.add_row("Temporal Resolution",
                      f"{cv['temporal_resolution']['value']} {cv['temporal_resolution']['unit']}")

        console.print(Panel(tree, title="Classification System"))
        console.print(table)

        console.print("[black]\tFinished![/black]")

    else:
        formatted_json = json.dumps(cv, indent=4, ensure_ascii=False)

        syntax = Syntax(formatted_json, "json", theme="monokai", line_numbers=True)
        console.print(f"\t[green bold]- Collection Metadata:[/green bold]")
        console.print(syntax)  # Pretty formatted JSON with syntax highlighting


@cli.command()
@click.option("-v", "--verbose", is_flag=True, default=False)
@click.option(
    "-a",
    "--collections",
    required=False,
    type=str,
    help="Collections list (items separated by comma)",
)
@click.option("--latitude", required=True, type=float, help="Latitude in EPSG:4326")
@click.option("--longitude", required=True, type=float, help="Longitude in EPSG:4326")
@click.option("--start-date", required=False, default=None, type=str, help="Start date")
@click.option("--end-date", required=False, default=None, type=str, help="End date")
@click.option("--language", required=False, default=None, type=str, help="Language")
@pass_config
def trajectory(
    config: Config,
    verbose,
    collections,
    start_date,
    end_date,
    latitude,
    longitude,
    language,
):
    """Return the trajectory associated to the location."""
    if verbose:
        console.print(f"[bold black]Server: [green]{config.url}[/green]")
        console.print("[black]\tRetrieving trajectory...[/black]")

    args = dict()
    if collections:
        args["collections"] = collections
    if start_date:
        args["start_date"] = start_date
    if end_date:
        args["end_date"] = end_date
    if language:
        args["language"] = language

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
    ) as progress:
        task = progress.add_task("[cyan]Processing trajectory request...", total=100)

        # Measure start time
        start_time = time()

        # Simulate progress
        for _ in range(5):
            progress.update(task, advance=20)

        # Retrieve trajectory data
        retval = config.service.tj(latitude=latitude, longitude=longitude, **args)

        # Measure end time
        end_time = time()

        # Calculate total time
        total_time = end_time - start_time

    # Display the trajectory data in a table format
    table = Table(title=f"Trajectory Results (Time: {total_time:.2f} seconds)")

    # Add table columns
    table.add_column("Class", style="cyan", no_wrap=True)
    table.add_column("Collection", style="magenta")
    table.add_column("Date", justify="right", style="green")
    table.add_column("Point ID", justify="right", style="yellow")

    # Add rows from the trajectory data
    for entry in retval.trajectory:
        table.add_row(
            entry["class"], entry["collection"], entry["date"], str(entry["point_id"])
        )

    # Display the table
    console.print(table)

    if verbose:
        console.print(f"[black]\tFinished in {total_time:.2f} seconds![/black]")
