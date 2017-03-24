#!/usr/bin/env python
import glob
import os
import sys
from os.path import splitext, basename

try:
    from setuptools import setup, Command, find_packages
except ImportError:
    from distutils.core import setup, Command, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    # noinspection PyAttributeOutsideInit
    def initialize_options(self):
        TestCommand.initialize_options(self)
        # Add any arguments here.
        self.pytest_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(name='foobar',
      version='0.0.1',
      author='Arxan Technologies, Inc.',
      author_email='devops@arxan.com',
      url='http://www.arxan.com',
      description='not the foobar music player',
      zip_safe=False,
      )

