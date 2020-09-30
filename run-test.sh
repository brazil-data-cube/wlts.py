#!/usr/bin/env bash
#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle wlts && \
isort --check-only --diff --recursive **/*.py && \
check-manifest --ignore ".travis-*,.readthedocs.yml"  && \
pytest && \
sphinx-build -qnW --color -b doctest doc/sphinx/ doc/sphinx/_build/doctest
