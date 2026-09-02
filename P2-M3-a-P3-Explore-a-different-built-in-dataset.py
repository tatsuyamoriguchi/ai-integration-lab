# P2-M3-P3-Explore-a-different-built-in-dataset.py
# 3. Explore a different built-in dataset Scikit-learn also has load_wine() and load_breast_cancer() 
# — load one of these, print its shape and target names, just to get comfortable with the pattern 
# being consistent across different datasets.

import sklearn
from sklearn.datasets import load_wine

wine = load_wine()

print("wine.data.shape")
print(wine.data.shape)
print("wine.target.shape")
print(wine.target.shape)
print("wine.feature_names")
print(wine.feature_names)
print("wine.target_names")
print(wine.target_names)

print(wine.data[:5])
print(wine.target[:5])


