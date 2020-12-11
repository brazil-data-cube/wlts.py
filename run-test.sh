#!/usr/bin/env bash
#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle wlts examples tests setup.py && \
isort wlts examples tests setup.py --check-only --diff && \
check-manifest --ignore ".travis-*" --ignore ".readthedocs.*" && \
pytest && \
sphinx-build -qnW --color -b doctest docs/sphinx/ docs/sphinx/_build/doctest
