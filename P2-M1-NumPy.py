import numpy as np

print("# PyNum List")
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print("")
print("# Python List")
arr = [1,2,3,4,5]
print(arr)

print("")
print("# Regular Python List")
prices = [100, 200, 300]
print(prices * 2)
# output = 0 Not necessary
output_arr = []
for item in prices:
    # output = item * 2
    # output_arr.append(output)
    output_arr.append(item * 2)

print(output_arr)

print("")
print("# NumPy array")
prices_np = np.array([100,200,300])
print(prices_np * 2)

print("")
print("# More Math")
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)
print(a * b)
print(b / a)

print("")
print("# Common Array Creation Helpers")
print(np.zeros(5))
print(np.ones(5))
print(np.arange(0,10,2))
print(np.linspace(0,1,5))
print(np.full(3, 5))

print("")
print("# Indexing and Slicing (familiar from Swift arrays, mostly)")
arr = np.array([10, 20, 30, 40, 50])
print(f"arr[0]: {arr[0]}")
print(f"arr[-1]: {arr[-1]}")  # 50 (last element — Python allows negative indexing)
print(f"arr[1:3]: {arr[1:3]}") # [20 30] (slice, like Swift's array[1..<3])

print("")
print("# 2D Arrays (Matrices) — This Is New Territory")
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix.shape)
print(matrix[0])
print(matrix[1,1])
print(matrix[1][1])
print(matrix[:, 1])

print(matrix.shape)   # (2, 3) → 2 rows, 3 columns
print(matrix[0])       # [1 2 3] — first row
print(matrix[0][1])    # 2 — row 0, column 1
print(matrix[:, 0])    # [1 4] — every row, column 0 (this slicing syntax is new)

print("")
print("Useful Aggregate Functions")
data = np.array([10, 20, 30, 40, 50])
print(data.sum())     # 150
print(data.mean())    # 30.0
print(data.max())     # 50
print(data.min())     # 10
print(data.std())     # standard deviation

days_since_response = np.array([2, 15, 30, 5, 45, 10])
print(days_since_response.mean())   # average wait time
print(days_since_response.std())    # how consistent/inconsistent response times are

print("")
print("Filtering with Boolean Conditions (very AI/data-science idiomatic)")

scores = np.array([55, 82, 91, 40, 76])
passing = scores[scores >= 60]
print(passing) # [82 91 76]