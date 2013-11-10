#!/usr/bin/env python

from distutils.core import setup

# FIXME: We will stick this shit here for now for the sake of running Travis CI.
__author__ = 'Sumin Byeon'
__email__ = 'suminb@gmail.com'
__version__ = '0.1.0'


def readme():
    try:
        f = open('README.rst')
        content = f.read()
        f.close()
        return content
    except IOError:
        pass
    except OSError:
        pass


setup(name='winnowing',
      version=__version__,
      description='A Python implementation of the Winnowing (local algorithms for document fingerprinting)',
      long_description=readme(),
      author=__author__,
      author_email=__email__,
      url='http://github.com/suminb/winnowing',
      packages=['winnowing'],
)

