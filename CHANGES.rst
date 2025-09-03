..
    This file is part of Python Client Library for WLTS.
    Copyright (C) 2024 INPE.

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


=======
Changes
=======

Version 1.3.1 (2025-09-03)
--------------------------

- Update project name - rename to wlts.py (`#101 <https://github.com/brazil-data-cube/wlts.py/issues/101>`_)
- Fixing lccs url in default command line (`#100 <https://github.com/brazil-data-cube/wlts.py/issues/100>`_)

Version 1.3.0 (2025-09-03)
--------------------------

- Update lccs.py version (`#95 <https://github.com/brazil-data-cube/wlts.py/issues/95>`_)
- Update plot to get color from LCCS  (`#97 <https://github.com/brazil-data-cube/wlts.py/issues/97>`_)
- Add support for numpy in lat long  (`#93 <https://github.com/brazil-data-cube/wlts.py/issues/93>`_)
- Collection parameter must accept a list of strings  (`#90 <https://github.com/brazil-data-cube/wlts.py/issues/90>`_)


Version 1.2.1 (2025-04-11)
--------------------------

- Bug fix: Update plotly to use new version of numpy and fixed bar plot (`#91 <https://github.com/brazil-data-cube/wlts.py/issues/91>`_)


Version 1.2.0 (2025-03-11)
--------------------------

- Add pyproject.toml (`#87 <https://github.com/brazil-data-cube/wlts.py/issues/87>`_)
- Change request to httpx (`#86 <https://github.com/brazil-data-cube/wlts.py/issues/86>`_)
- Add support for lccs 1.0.0 (`#85 <https://github.com/brazil-data-cube/wlts.py/issues/85>`_)
- Improve command line interface (`#83 <https://github.com/brazil-data-cube/wlts.py/issues/83>`_)


Version 1.1.0 (2024-08-01)
--------------------------

- Update lccs version with support to INPE Identity Access Management (`#80 <https://github.com/brazil-data-cube/wlts.py/issues/80>`_)


Version 1.0.1 (2023-11-29)
--------------------------

- Change license to GPLv3 (`#67 <https://github.com/brazil-data-cube/wlts.py/issues/67>`_).

- Update lccs.py version to 0.8.2 (`#69 <https://github.com/brazil-data-cube/wlts.py/issues/69>`_).

- Bug fix: in trajectory harmonize change system source to id (`#71 <https://github.com/brazil-data-cube/wlts.py/issues/71>`_).

- Review of code examples (`#72 <https://github.com/brazil-data-cube/wlts.py/issues/72>`_).

Version 1.0.0 (2022-08-25)
--------------------------

- Review documentation (`#64 <https://github.com/brazil-data-cube/wlts.py/issues/64>`_).

- Review command line (`#62 <https://github.com/brazil-data-cube/wlts.py/issues/62>`_).

- Update trajectory item template (`#61 <https://github.com/brazil-data-cube/wlts.py/issues/61>`_).

- Add update traces in bar plot (`#60 <https://github.com/brazil-data-cube/wlts.py/issues/60>`_).

- Add support for LCCS-DB version 0.8.1 (`#57 <https://github.com/brazil-data-cube/wlts.py/issues/57>`_).

- Add support for internationalization.

- Add scatter plot (`#56 <https://github.com/brazil-data-cube/wlts.py/issues/56>`_).

- Add bar plot for support trajectories of with multiples collections and points. (`#55 <https://github.com/brazil-data-cube/wlts.py/issues/55>`_).

Version 0.8.0 (2021-09-30)
--------------------------

- Use the access_token in WLTS request (`#47 <https://github.com/brazil-data-cube/wlts.py/issues/47>`_).

- Integration with the Land Cover Classification System Web Service (LCCS.py) (`#12 <https://github.com/brazil-data-cube/wlts.py/issues/12>`_).


Version 0.6.0 (2021-04-13)
--------------------------

- Add Drone integration (`#38 <https://github.com/brazil-data-cube/wlts.py/issues/38>`_).

- Integration with Geopandas package (`#33 <https://github.com/brazil-data-cube/wlts.py/issues/33>`_).

- Add support for user pass multiple points in trajectory (`#42 <https://github.com/brazil-data-cube/wlts.py/issues/42>`_).

- Improve Jupyter integration (`#33 <https://github.com/brazil-data-cube/wlts.py/issues/33>`_).

- Add Jupyter support to WLTS objects (`#44 <https://github.com/brazil-data-cube/wlts.py/issues/44>`_).

Version 0.4.0-0 (2020-12-15)
----------------------------

- Basic integration with Jupyter Environment and Pandas.

- Command Line Interface (CLI).

- Support for the `WLTS specification version 0.4.0-0 <https://github.com/brazil-data-cube/wlts-spec>`_.

- Documentation system based on Sphinx.

- Documentation integrated to ``Read the Docs``.

- Installation and build instructions.

- Package support through Setuptools.

- Installation and usage instructions.

- Travis CI support.

- Source code versioning based on `Semantic Versioning 2.0.0 <https://semver.org/>`_.

- License: `MIT <https://github.com/gqueiroz/wtss.py/blob/master/LICENSE>`_.
