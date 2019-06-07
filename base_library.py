''' Basic libraries
    . scikit-learn: It contains a lot of state-of-the-art machine learning
      algorithms.

    . Numpy: It is the fundamental packages for scientific computing in Python.
    . Scipy: It is a collection of functions for scientific computing in Python.
    . marplotlib: It is the primary scientific plotting library in Python.
    . pandas: It is a Python library for data wrangling and analysis.
'''
import os
import sys
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib
import IPython
import sklearn

# show the version of each library
print('Python version: {}'.format(sys.version))
print('Numpy version: {}'.format(np.__version__))
print('Scipy version: {}'.format(sp.__version__))
print('Pandas version: {}'.format(pd.__version__))
print('Matplotlib version: {}'.format(matplotlib.__version__))
print('IPython version: {}'.format(IPython.__version__))
print('scikit-learn version: {}'.format(sklearn.__version__))