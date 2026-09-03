# 2. Perform a train/test split 
# Split the iris data into training and test sets, using test_size=0.25 (25% held out) 
# and random_state=42. Print the shape of all four resulting arrays (X_train, X_test, y_train, y_test) to confirm the split sizes.

import sklearn

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

iris = load_iris()

(X_train, X_test, y_train, y_test) = train_test_split(
    iris.data,
    iris.target,
    test_size=0.25,
    random_state=42
)

print("X_train.shape")
print(X_train.shape)
print("X_test.shape")
print(X_test.shape)
print("y_train.shape")
print(y_train.shape)
print("y_test.shape")
print(y_test.shape)

