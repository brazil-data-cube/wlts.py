..
    This file is part of Web Land Trajectory Service.
    Copyright (C) 2019-20 INPE.

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

      [{'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2007'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2008'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2009'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2010'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2011'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2012'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2013'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2014'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2015'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2016'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2017'},
     {'class': 'Formação Florestal',
      'collection': 'mapbiomas_amz_4_1',
      'date': '2018'}]



.. code-block:: shell

        wlts-cli --url 'http://localhost/wlts' trajectory --geoloc 0 0

or:

.. code-block:: shell

        wlts-cli --url 'http://localhost/wlts' trajectory --ifile query.json


