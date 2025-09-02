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
"""Utility functions for WLTS client library."""
from importlib.resources import files
from typing import Any

import jinja2

template_dir = files("wlts").joinpath("templates")
templateLoader = jinja2.FileSystemLoader(str(template_dir))
templateEnv = jinja2.Environment(loader=templateLoader)


class Utils:
    """A class that represents a Utils in WLTS."""

    @staticmethod
    def render_html(template_name: str, **kwargs: Any) -> str:
        """
        Render a Jinja2 HTML template.

        Args:
            template_name (str): The name of the template file to render.
            **kwargs (Any): Arbitrary keyword arguments to be passed to the template.

        Returns:
            str: The rendered HTML as a string.
        """
        template = templateEnv.get_template(template_name)
        return template.render(**kwargs)

    @classmethod
    def update_column_title(cls, title):
        """Update the collection name with spaces and capitalize."""
        new_title = (title.text.split("=")[-1]).capitalize()

        if len(new_title.split("_")) > 1:
            return new_title.split("_")[0] + " " + new_title.split("_")[-1].capitalize()

        return new_title.split("_")[0]