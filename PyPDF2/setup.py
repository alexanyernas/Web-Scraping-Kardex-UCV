#!/usr/bin/env python

import re

from setuptools import setup

VERSIONFILE = "PyPDF2/_version.py"
with open(VERSIONFILE) as fh:
    verstrline = fh.read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSIONFILE}.")

setup(version=verstr, package_data={"PyPDF2": ["*.typed"]})
