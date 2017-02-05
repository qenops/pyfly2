#!/usr/bin/env python

# Build the pyd with 
#   python setup.py build_ext --inplace
# 

# from setuptools import setup, Extension
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

import os.path

desc = """This is Keith Brafford's first attempt at
a wrapper for the FlyCapture2 C API.
"""

fc2_lib = ''

if os.name=='posix':
    fc2_inc='/usr/include/flycapture'
    fc2_shared='flycapture-c'
    fc2_lib='/usr/lib'
    data_files=[]
else:
    # Windows
    if os.path.exists('C:/Program Files (x86)/Point Grey Research/FlyCapture2'):
        fc2_sdk = 'C:/Program Files (x86)/Point Grey Research/FlyCapture2'
    else:
        fc2_sdk = 'C:/Program Files/Point Grey Research/FlyCapture2'

    if os.path.exists(os.path.join(fc2_sdk, 'lib/vs2015')):
        fc2_lib = os.path.join(fc2_sdk, 'lib/vs2015')
    elif os.path.exists(os.path.join(fc2_sdk, 'lib64/vs2015')):
        fc2_lib = os.path.join(fc2_sdk, 'lib64/vs2015')

    fc2_shared = 'FlyCapture2_Cd_v140'
    # fc2_shared = 'FlyCapture2_C_v140'
    data_files=['FlyCapture2_C_v140.dll', 'FlyCapture2_v140.dll', 'libiomp5md.dll']
    # data_files=['FlyCapture2_C_v90.dll', 'FlyCapture2_v90.dll',  'libiomp5md.dll']

    fc2_inc = [os.path.join(fc2_sdk, 'include')]

ext = [Extension('pyfly2', ['pyfly2.pyx'],
                 include_dirs= fc2_inc,
                 libraries=['FlyCapture2_C_v140'],
                 library_dirs=[fc2_lib],
                 extra_compile_args=['/Zi'],
                 extra_link_args=['/debug'],
                 )
       ]

setup(name='pyfly2',
      version='0.2',
      author='Keith Braddord',
      license='BSD',
      description=desc,
      ext_modules=cythonize(ext),
      requires=['Cython', 'numpy'],
      data_files=data_files
      )
