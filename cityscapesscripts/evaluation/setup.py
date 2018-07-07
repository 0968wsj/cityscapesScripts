#!/usr/bin/python
#
# Enable cython support for eval scripts
# Run as
# setup.py build_ext --inplace
#
# WARNING: Only tested for Ubuntu 64bit OS.

try:
    from distutils.core import setup
    from Cython.Build import cythonize
except Exception as e:
    print("Unable to setup. Please use pip to install: cython")
    print("sudo pip install cython")
    print(e)
import os
import numpy

os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

setup(ext_modules=cythonize("addToConfusionMatrix.pyx"), include_dirs=[numpy.get_include()])
