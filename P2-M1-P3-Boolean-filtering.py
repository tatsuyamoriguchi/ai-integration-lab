# P2-M1-P3-Boolean-filtering.py
import numpy as np

# 3. Boolean filtering 
# Create an array of 6 "days since last response" values for different job applications 
# (e.g., [2, 15, 30, 5, 45, 10]). Filter and print only the ones greater than 14 days 
# (a signal that you should follow up).

days_sinceLast_response = np.array([2, 15, 30, 5, 45, 10])
late_response = days_sinceLast_response[days_sinceLast_response > 14]
print(late_response)

