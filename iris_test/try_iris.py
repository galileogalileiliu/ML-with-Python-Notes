''' Try some properties of iris data set
'''
from sklearn.datasets import load_iris
iris_data = load_iris()
# iris_data is a numpy.ndarray

# Show how many keys(or metadata) of iris dataset
print('Keys of iris_data: {}'.format(iris_data.keys()))
# show each property of key
# DESCR: Descriptions
print('Iris data: {}'.format(iris_data['DESCR'][:193])+ '\n...')
# Target Name
print('Iris Target Name: {}'.format(iris_data['target_names']))
# Features
print('Iris Feature Name: {}'.format(iris_data['feature_names']))
# Show the data type of Iris_Data
print('Iris data type: {}'.format(type(iris_data['data'])))
# Data Shape: Shows how many data and how many features of each data
# In the cases, there are 150 records and 4 features of each record.
# So it may be image as a two dimension array.
# ex. [[5.1 3.5 1.4 0.2]  [4.9 3.  1.4 0.2] [4.7 3.2 1.3 0.2]....]
# This information also can be found in the DESCR
print('Iris data shape: {}'.format(iris_data['data'].shape))
print('The data shape of Iris is (150.4), this means that')
print('there are 150 records in iris_data and 4 features of each record')
print('In machine learning, we call them sample and features.')
print('That is, 150 sample and 4 features of each sample.')
