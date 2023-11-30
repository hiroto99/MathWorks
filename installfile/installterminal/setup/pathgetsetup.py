from distutils.core import setup, Extension
from Cython.Build import cythonize
import os

module = Extension("getpath", sources=["installfile/installterminal/bin/getpath.pyx"], include_dirs=[])
i = setup(name="getpath", ext_modules=cythonize([module]))