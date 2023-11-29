..
    This file is part of Python Client Library for WLTS.
    Copyright (C) 2023 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.


=====================================================
Python Client Library for Web Land Trajectory Service
=====================================================

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
        :target: https://github.com/brazil-data-cube/wlts.py/blob/master/LICENSE
        :alt: Software License

.. image:: https://readthedocs.org/projects/wlts/badge/?version=latest
        :target: https://wlts.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. .. image:: https://img.shields.io/badge/pypi-v0.1.0-informational
        :target: https://pypi.org/pypi/wlts.py

.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
        :target: https://www.tidyverse.org/lifecycle/#maturing
        :alt: Software Life Cycle

.. image:: https://img.shields.io/github/tag/brazil-data-cube/wlts.py.svg
        :target: https://github.com/brazil-data-cube/wlts.py/releases
        :alt: Release

.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord

About
=====

Land Use and Cover information is essential to support governments in decision making on the impact of human activities on the environment, for planning the use of natural resources, conservation of biodiversity, and monitoring climate change.


Currently, several projects systematically provide information on the dynamics of land use and cover. Well known projects include PRODES, DETER and TerraClass. These projects are developed by INPE and they produce information on land use and coverage used by the Brazilian Government to make public policy decisions. Besides these projects there are other initiatives from universities and space agencies devoted to the creation of national and global maps.


Although these projects adhere to open data policies and provide a rich collection of data, there are still a gap however in tools that facilitate the integrated use of these collections: *it requires from researchers, students and public officials a great effort to collect, organize and integrate all the datasets, prior to their use*. In general, each data collection adopts its own land use and cover classification system, with class names and meanings very different across the collections. Besides that, the collections have different spatial and temporal resolutions, rely on different data representation (raster or vector), and are served by different systems in several formats (files, DBMS or web services).


In this context, the **W**\ eb **L**\ and **T**\ rajectory **S**\ ervice (WLTS) is a service that aims to facilitate the access to these various land use and cover data collections through a tailored API. The result is tool that allows researchers and specialists to spend their time in the analytical process, once the API provides the integration of these datasets and brings the concept of Land Use and Cover Trajectories as a high level abstraction. The WLTS approach is to use a data model that defines a minimum set of temporal and spatial information to represent different sources and types of data. WLTS can be used in a range of application, such as in validation of land cover data sets, in the selection of trainning samples to support Machine Learning algorithms used in the generation of new classification maps.

WLTS is based on three operations:

- list_collections: return the list of all available collections in the service.
- describe_collection: return the metadata of a given data collection.
- trajectory: return the land use and cover trajectories from the collections given a location in space. The property result contains the feature identifier information, class, time, and the collection associated to the data item.

If you want to know more about WLTS service, please, take a look at its `specification <https://github.com/brazil-data-cube/wlts-spec>`_.

Installation
============

See `INSTALL.rst <./INSTALL.rst>`_.


Using WLTS in the Command Line
==============================

See `CLI.rst <./CLI.rst>`_.


Developer Documentation
=======================

See https://wlts.readthedocs.io/en/latest.


License
=======

.. admonition::
    Copyright (C) 2023 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
