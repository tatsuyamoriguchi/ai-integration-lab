# 1. Load and explore Load the iris dataset. Print .data.shape, .target.shape, .feature_names, and .target_names.
# In a comment, write one sentence describing what each of the 4 features seems to measure, based on the names.

import sklearn

from sklearn.datasets import load_iris
iris = load_iris()

print("iris.data.shape: Measures the number of column and rows")
print(iris.data.shape)
print("iris.target.shape: Measures the number of rows")
print(iris.target.shape)
# print("iris.feature_names: X_train and X_test") <- Wrong!
print("iris.feature_names: what each of the 4 measurement columns represents")
print(iris.feature_names)
# print("iris.target_names: y_train and Y-test") -> Wrong!
print("iris.target_names: what each species number (0, 1, 2) represents")
print(iris.target_names)
