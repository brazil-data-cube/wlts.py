..
    This file is part of Web Land Trajectory Service.
    Copyright (C) 2019 INPE.

    Web Land Trajectory Service is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Running WLTS Client in the Command Line
=======================================

List the available collections:

.. code-block:: shell

        wlts-cli --url 'http://localhost/wlts' collections


Retrieve the trajactory given a longitude and latitude:

.. code-block:: shell

        wlts-cli --url 'http://localhost/wlts' trajectory -- 0 0

The above command will return a JSON document as:

.. code-block:: shell

        {
            'query': {
                'collections': None,
                'end_date': None,
                'latitude': -12.0,
                'longitude': -54.0,
                'start_date': None
            },
            'result': {
                'trajectory': [{
                        'class': 'Floresta',
                        'collection': 'terraclass',
                        'date': '2004'
                    },
                    {
                        'class': 'Floresta',
                        'collection': 'terraclass',
                        'date': '2008'
                    },
                    {
                        'class': 'Floresta',
                        'collection': 'terraclass',
                        'date': '2010'
                    },
                    {
                        'class': 'Floresta',
                        'collection': 'terraclass',
                        'date': '2012'
                    },
                    {
                        'class': 'Floresta',
                        'collection': 'terraclass',
                        'date': '2014'
                    },
                    {
                        'class': 'Floresta',
                        'collection': 'prodes',
                        'date': '2017'
                    }
                ]
            }
        }



.. code-block:: shell

        wlts-cli --url 'http://localhost/wlts' trajectory --geoloc 0 0

or:

.. code-block:: shell

        wlts-cli --url 'http://localhost/wlts' trajectory --ifile query.json


