#!/usr/bin/env python
import os
import sys
import codecs

try:
	from setuptools import setup, find_packages
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, find_packages

import moat as distmeta

packages, data_files = find_packages(exclude=("example_project",)), []
root_dir = os.path.dirname(__file__)
if root_dir != '':
	os.chdir(root_dir)
src_dir = "moat"


if os.path.exists("README.rst"):
	long_description = codecs.open("README.rst", "r", "utf-8").read()
else:
	long_description = "See http://amrox.github.com/django-moat/"


setup(
	name='django-moat',
	version=distmeta.__version__,
	description=distmeta.__doc__,
	author=distmeta.__author__,
	author_email=distmeta.__contact__,
	url=distmeta.__homepage__,
	platforms=["any"],
	# license="BSD",
	packages=packages,
	data_files=data_files,
	long_description=long_description,
)
