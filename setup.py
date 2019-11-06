#
# This file is part of Web Land Trajectory Service.
# Copyright (C) 2019 INPE.
#
# Web Land Trajectory Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Python Client Library for the Web Land Trajectory Service."""

import os
from setuptools import find_packages, setup

readme = open('README.rst').read()

history = open('CHANGES.rst').read()

tests_require = [
]

extras_require = {
    'docs': [
        'Sphinx',
    ],
}

setup_requires = [
]

install_requires = [
]

packages = find_packages()

with open(os.path.join('wlts', 'version.py'), 'rt') as fp:
    g = {}
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='wlts',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='Land Use FOSS',
    license='MIT',
    author='INPE',
    author_email='fabi.zioti@gmail.com',
    url='https://github.com/brazil-data-cube/wlts.py',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)