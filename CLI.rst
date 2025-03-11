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


Running WLTS Client in the Command Line
=======================================

The ``WLTS`` client installs a command line tool named ``wlts-cli`` that allows to retrieve trajectory data.


If you want to know the WLTS version, use the option ``--version`` as in::

    wlts-cli --version


List the available collections::

    wlts-cli --url 'https://data.inpe.br/bdc/wlts/v1' list-collections


To get more information about a specific collection, use the ``describe`` command::

    wlts-cli --url 'https://data.inpe.br/bdc/wlts/v1' describe --collection prodes_amazonia_legal


Retrieve the trajectory given a longitude and latitude::

    wlts-cli --url 'https://data.inpe.br/bdc/wlts/v1' \
             --access-token='change-me' \
             trajectory \
             --latitude -12.0 \
             --longitude -54.0  \
             --start-date 2001 \
             --end-date 2011 \
             --collections mapbiomas-v9


The above command will return a document as:

.. code-block:: shell

       trajectory: [
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2001'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2002'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2003'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2004'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2005'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2006'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2007'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2008'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2009'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2010'},
        {'class': 'Formação Florestal', 'collection': 'mapbiomas-v9', 'date': '2011'}
       ]

.. note::

    You may need to pass the parameter ``--access-token=CHANGE_ME`` to retrieve trajectory.

