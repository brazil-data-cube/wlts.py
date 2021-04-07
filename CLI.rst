..
    This file is part of Python Client Library for WLTS.
    Copyright (C) 2020-2021 INPE.

    Python Client Library for WLTS is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Running WLTS Client in the Command Line
=======================================

List the available collections::

    wlts-cli --url 'https://brazildatacube.dpi.inpe.br/wlts/' collections


Retrieve the trajectory given a longitude and latitude::

    wlts-cli --url 'https://brazildatacube.dpi.inpe.br/wlts/' trajectory -- 0 0

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

You can also use::

    wlts-cli --url 'https://brazildatacube.dpi.inpe.br/wlts/' trajectory --geoloc 0 0

or pass a json file with the location in space::

    wlts-cli --url 'https://brazildatacube.dpi.inpe.br/wlts/' trajectory --ifile query.json


