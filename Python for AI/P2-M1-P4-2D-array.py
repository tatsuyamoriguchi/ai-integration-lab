# P2-M1-P4-2D-array.py
import numpy as np

# 4. 2D array practice 
# Create a 2D array representing 3 job applications, each with 2 values: 
# [days_since_applied, days_since_last_contact]. Print the shape, then print just 
# the first column (days_since_applied for all applications) using the [:, 0]slicing syntax.

data = np.array([
    [1, 5],
    [3, 10],
    [35, 9]
])

print(data.shape)
print(data[:, 0])
print(data[:, 1])
