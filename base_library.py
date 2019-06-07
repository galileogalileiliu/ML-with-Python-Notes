''' Basic libraries
    . scikit-learn: It contains a lot of state-of-the-art machine learning
      algorithms.

    . Numpy: It is the fundamental packages for scientific computing in Python.
    . Scipy: It is a collection of functions for scientific computing in Python.
    . marplotlib: It is the primary scientific plotting library in Python.
    . pandas: It is a Python library for data wrangling and analysis.

    Numpy version: 1.16.2
    Scipy version: 1.2.1
    Pandas version: 0.24.2
    Matplotlib version: 3.0.3
    IPython version: 7.4.0
    scikit-learn version: 0.20.3
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

# test how to push to github
# test how to push to github2
# test how to push to github3
# In VS Code, need to add remark message, click command+Enter
# Then exec 'Push'
# Git will then really push the change to the github
# These two steps must be together.