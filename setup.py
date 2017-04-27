# -*- coding: utf-8 -*-
import sys

#from distutils.core import setup
from setuptools import setup

long_description='''\
Overview
========

This package can be used to control and record data from a Tektronix scope.
Communication relies on the USBTMC GNU/Linux device driver thus avoiding the installation of VISA. 

The package is an adaptation of PyTektronixScope by Pierre Cladé based on VISA.


Installation
============

To use the USBTMC device driver GNU/Linux in Debian its permissions should be set at `/lib/udev/rules.d/40-usbtmc-permissions.rules` to

  # Devices
  KERNEL=="usbtmc/*",
  KERNEL=="usbtmc[0-9]*",
  MODE="0660", GROUP="usbtmc"
  MODE="0660", GROUP="usbtmc"

A replace-in permissions file is provided.

To install pyTekRealTimeUSBTMC, download the package and run the command:: 

  python setup.py install

Alternatively the pyTektronixScope directory can manually be moved to a location that Python can import from.

Sources can also be download on the `pyTektronixScopeUSBTMC github repository`_. 

Usage
=====

Typical usage::

  from pyTekScopeUSBTMC import TektronixScopeUSBTMC
  scope = TektronixScopeUSBTMC("/dev/usbtmc0")

  X,Y = scope.read_data_one_channel('CH2', t0 = 0, DeltaT = 1E-6, x_axis_out=True)

Contact
=======

Please send bug reports or feedback to `Victor Bettachini`_.


Version history
===============
Main changes:

* 0.1 Initial relase

.. _Victor Bettachini: mailto:victorb@gmx.net
.. _PyTektronixScopeUSBTMC github repository: https://github.com/bettachini/PyTektronixScope
'''
setup(name="PyTektronixScope", version='0.1',
author=u'Víctor Bettachini', author_email="victorb@gmx.net",
maintainer=u'Víctor Bettachini', maintainer_email="victorb@gmx.net",
url='https://github.com/bettachini/PyTektronixScope',
license='''\
This software can be used under one of the following two licenses: \
(1) The BSD license. \
(2) Any other license, as long as it is obtained from the original \
author.''',
description='Interface to Tektronix Scope',
long_description = long_description,  
keywords=['Tektronix', 'scope', 'Data Acquisition'],
classifiers=[
'Development Status :: 1 - Beta',
'Intended Audience :: Developers',
'Intended Audience :: Education',
'Intended Audience :: Other Audience',
'Intended Audience :: Science/Research',
'License :: OSI Approved :: BSD License',
'Programming Language :: Python',
'Topic :: Scientific/Engineering',
'Topic :: Scientific/Engineering :: Physics',
'Topic :: Software Development',
'Topic :: Software Development :: Libraries',
'Topic :: Software Development :: Libraries :: Python Modules'], 
packages=["pyTektronixScope:"]
