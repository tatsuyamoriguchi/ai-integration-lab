import numpy as np

# 1. Basic array + vectorized math 
# Create a NumPy array of 5 numbers representing days of job applications sent 
# (e.g., [3, 5, 2, 4, 6]). Multiply the whole array by 2 (simulating doubling your outreach), 
# and print the result.

days_array_np = np.array([3, 5, 2, 4, 6])
print(days_array_np * 2)
