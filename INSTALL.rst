..
    This file is part of Web Land Trajectory Service.
    Copyright (C) 2019-2020 INPE.

    Web Land Trajectory Service is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Installation
============

``wlts.py`` depends essentially on `Requests <https://requests.readthedocs.io/en/master/>`_. Please, read the instructions below in order to install ``wlts.py``.


Production installation
-----------------------

**Under Development!**

.. Install from `PyPI <https://pypi.org/>`_:
..
.. .. code-block:: shell
..
..     $ pip3 install wlts.py


Development Installation - GitHub
---------------------------------

Clone the Software Repository:

.. code-block:: shell

        $ git clone https://github.com/brazil-data-cube/wlts.py.git


Go to the source code folder:

.. code-block:: shell

        $ cd wlts.py


Install in development mode:

.. code-block:: shell

        $ pip3 install -e .[all]


Run the Tests
+++++++++++++


.. code-block:: shell

        $ ./run-test.sh

Build the Documentation
+++++++++++++++++++++++

You can generate the documentation based on Sphinx with the following command::

    python setup.py build_sphinx


The above command will generate the documentation in HTML and it will place it under::

    docs/sphinx/_build/html/


You can open the above documentation in your favorite browser, as::

    firefox docs/sphinx/_build/html/index.html
