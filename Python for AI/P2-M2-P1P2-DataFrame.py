# P2-M2-P1-DataFrame.py
# 1. Build a DataFrame 
# Create a DataFrame from your job applications list (5 entries, with company, role, status, and days_since_applied as columns). 
# Print it, then print .shape and .columns.

import pandas as pd

applications = [
    {"company": "MSP A Co.", "role": "Sales Engineer", "status": "Applied", "days_since_applied": 2},
    {"company": "MSP B Co.", "role": "Sr. Sales Engineer", "status": "Recruiter's Screening", "days_since_applied": 5},
    {"company": "MSP C Co.", "role": "Solutions Engineer", "status": "Applied", "days_since_applied": 3},
    {"company": "MSP D Co.", "role": "Solutions Architect", "status": "Rejected", "days_since_applied": 14},
    {"company": "MSP E Co.", "role": "Sr. Solutions Engineer", "status": "Hiring Manager Interview", "days_since_applied": 10}
    ]

df = pd.DataFrame(applications)
print(df)
print(df.shape)
print(df.columns)

# 2. Inspect it Run .info() and .describe() on your DataFrame. 
# (Note: .describe() will only show stats for the numeric column 
# — that's expected.)
print("")
print("df.info():")
print(df.info())
print("")
print("df.describe():")
print(df.describe())

# 3. Filter with boolean masking Filter and print only the applications where status == "Rejected".
print("")
print("DataFrame Filter")
rejected = df[df["status"] == "Rejected"]
print(rejected)

# 4. Add a computed column Add a new column follow_up_needed that's True if days_since_applied > 14, else False.
print("")
print("Add a new Column")
# The following is totally wrong!
# df.columns.append("follow_up_needed", int)
# df.columns.append("days_since_applied", bool)

# for app in df.applications:
#     if app[days_since_applied] > 14:
#         app["follow_up_needed"] = True
# else:
#     app["follow_up_needed"] = False

# print(df.applications)

df["follow_up_needed"] = df["days_since_applied"] > 14
print(df)

# my_dict = {"a": 1, "b": 2}
# my_dict["c"] = 3          # "c" didn't exist before — this just CREATES it
# print(my_dict)             # {'a': 1, 'b': 2, 'c': 3}

# 5. Clean messy data 
# I'll give you a deliberately messy dataset (extra whitespace, inconsistent casing, a missing value) — clean it using 
# .str.strip(), .str.lower(), and .fillna().

applications2 = [
    {"company": " MSP A Co.", "role": "Sales Engineer", "status": "Applied", "days_since_applied": 2},
    {"company": "MSP B Co. ", "role": "Sr. Sales Engineer", "status": "Recruiter's Screening", "days_since_applied": 5},
    {"company": "MSP C Co.", "role": "solutions Engineer", "status": "Applied", "days_since_applied": 3},
    {"company": "MSP D Co.", "role": "Solutions architect", "status": "Rejected", "days_since_applied": 14},
    {"company": "MSP E Co.", "role": "Sr. Solutions Engineer", "status": None, "days_since_applied": 10}
]

df2 = pd.DataFrame(applications2)
print("")
print("Add Unknown to missing values")
df2_clean = df2.fillna("Unknown")
print("Original df2:")
print(df2)
print("After dropna():")
print(df2_clean)

print("")
print("Strip white spaces")
df2_clean["company"] = df2_clean["company"].str.strip()
print("Original df2:")
print(df2)
print("After strippiing white spaces by .str.strip()")
print(df2_clean)

print("")
print("Fix incosnsistent case")
df2_clean["role"] = df2_clean["role"].str.lower()
print("Original df2:")
print(df2)
print("After str.lower()")
print(df2_clean)