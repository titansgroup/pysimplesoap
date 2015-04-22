#!/usr/bin/env python

from distutils.core import setup
try:
    from nsis import build_installer
except:
    build_installer = None

from pysimplesoap import __author__, __author_email__, __license__

# in the transition, register both:
setup(
    name='tg-pysimplesoap',
    version='0.0.1',
    description='Python simple and lightweight SOAP Library',
    author=__author__,
    author_email=__author_email__,
    url='http://code.google.com/p/pysimplesoap',
    packages=['pysimplesoap'],
    license=__license__,
    cmdclass={"py2exe": build_installer},
)
