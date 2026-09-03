# Phase 2: Python for AI/ML Basics (continued)
# Module 3: Intro to a model framework — scikit-learn 

import sklearn

print("Loading a Built-in Dataset")
# The classic "Iris" dataset: 150 flower measurements (petal length, petal width, sepal length, sepal width), 
# each labeled with which of 3 species it is. The task: given measurements, predict the species.

from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data[:5]) # first 5 rows
print(iris.target[:5]) # first 5 labels (what we are trying to predict)
print(iris.feature_names) # names of each feature/column
print(iris.target_names) # names of each possible label/class

print("")
print("Understanding the Data Shape")
print("iris.data.shape")
print(iris.data.shape)
print("iris.target.shape")
print(iris.target.shape)

print("")
import numpy as np
flat = np.array([1, 2, 3])
print("flat.shape")
print(flat.shape)

column = np.array([[1], [2], [3]])
print("column.shape")
print(column.shape)

print("flat[0]")
print(flat[0]) # 1
print("column[0]")
print(column[0]) # [1] 

print("")
print("Train/Test Split")
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    random_state=42
)

print(X_train.shape) # (120, 4) - 80% of data, for training
print(X_test.shape) # (30, 4) - 20% of data, held back for testing

