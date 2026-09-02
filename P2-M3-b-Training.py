# P2-M3-b-Training.py
# Section 1: Choosing and creating a model

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    random_state=42
)

# Section 1: Choosing and creating a model
print("Section 1: Choosing and creating a model")

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=200)

# Section 2: Training the model — .fit()
print("Section 2: Training the model — .fit()")
model.fit(X_train, y_train)
print("")
print("Model Trained Successfully")
print(model)

# Section 3: Making predictions — .predict()
print("")
print("Section 3: Making predictions — .predict()")
predictions = model.predict(X_test)
print(predictions)
print("Predictions:", predictions)
print("Actual:     ", y_test)

# Section 4: Checking accuracy
print("")
print("Section 4: Checking accuracy")
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

accuracy2 = model.score(X_test, y_test)
print(f"Accuracy 2: {accuracy2}")
