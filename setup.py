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

docs_require = [
    'Sphinx>=2.2',
]

tests_require = [
    'coverage>=4.5',
    'coveralls>=1.8',
    'pytest>=5.2',
    'pytest-cov>=2.8',
    'pytest-pep8>=1.0',
    'pydocstyle>=4.0',
    'isort>4.3',
    'check-manifest>=0.40',
    'requests-mock>=1.7.0'
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
    'pandas': ['pandas>=1.1']
}

extras_require['all'] = [ req for exts, reqs in extras_require.items() for req in reqs ]

setup_requires = [
    'pytest-runner>=5.2',
]

install_requires = [
    'requests>=2.20',
    'Click>=7.0',
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
    keywords=['Land Use Land Cover', 'GIS', 'Web Services', 'WFS', 'WCS', 'WTSS'],
    license='MIT',
    author='INPE',
    author_email='fabi.zioti@gmail.com',
    url='https://github.com/brazil-data-cube/wlts.py',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'wlts-cli = wlts.cli:cli',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
