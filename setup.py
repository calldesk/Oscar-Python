#!/usr/bin/env python

from setuptools import setup, find_packages

import Oscar

setup(
      name='Oscar',
      packages=find_packages(),
      author="SensOut",
      author_email="@SensOut",
      description="Oscar's Python client",
      long_description=open('README.md').read(),
      # take into account MANIFEST.in
      include_package_data=True,
      url='http://oscar.sensout.com'
      )