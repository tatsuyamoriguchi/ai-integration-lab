# P2-M2-Pandas.py
import pandas as pd

# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)

print("Creating a DataFrame")
applications = [
    {"company": "MSP A Co.", "role": "Sr. Solutions Engineer", "status": "Applied"},
    {"company": "MSP B Co.", "role": "Sales Engineer", "status": "Recruiter's Screening"},
    {"company": "MSP C Co.", "role": "Implementation Engineer", "status": "Rejected"}
]

df = pd.DataFrame(applications)
print(df)

print("")
print("Reading Real Files")
df = pd.read_csv("job_applications.csv")

print("")
print("Inspecting a DataFrame")
print(f"df.head(): {df.head()}")
print("")
print(f"df.tail(): {df.tail()}")
print("")
print(f"df.shape: {df.shape}")
print("")
print(f"df.columns: {df.columns}")
print("")
# print(f"df.info(): {df.info()}")
print("df.info: ")
print(df.info)
print(f"df.describe(): {df.describe()}")

print("")
print("Selecting Columns")
print(f'df[\"Company\"]: {df["Company"]}')
print(f'df[[\"Company\", \"Current Status\"]]): {df[["Company", "Current Status"]]}')

print("")
print("Selecting Rows")
print(f'df.iloc[0]:')
print(df.iloc[0])
print(f'df.loc[0]:')
print(df.loc[0])

print("")
print("Custom Indexing")
# df = pd.read_csv("job_applications.csv")
df_custom = df.set_index("Company")
print(f'df_custom:')
print(df_custom)
print(f'df_custom.iloc[0]:')
print(df_custom.iloc[0])
print(f'df_custom.loc["Tailor]:')
print(df_custom.loc["Tailor"])

print("")
print("Boolean Filtering")
rejected = df[df["Current Status"] == "Rejected"]
print("rejected")
print(rejected)

print("Adding a New Column")
df["needs_follow_up"] = df["Current Status"] == "Applied"
print(df)
print("")
print("Saving to New File")


print("")
print("Handling missing values")
print(df.isna())
print(df.isna().sum())

df_clean = df.dropna()
print(f"Original rows: {len(df)}")
print(f"After dropna(): {len(df_clean)}")

df_clean = df.fillna("Unknown")
print(f"Original rows: {len(df)}")
print(f"After dropna(): {len(df_clean)}")

print("")
print("Removing duplicates")
print("df_deduped = df.drop_duplicates()")
df_deduped = df.drop_duplicates()

print("")
print("Renaming columns")
df_clean = df_clean.rename(columns={"Company": "company_name"})

print("")
print("Calulate numbers of days since appiled")
df_clean["Date"] = pd.to_datetime(df_clean["Date"], errors="coerce")
today = pd.Timestamp.now()
df_clean["days_since_applied"] = (today - df_clean["Date"]).dt.days
print("Changing a column's data type")

print("")
df_clean["days_since_applied"] = df_clean["days_since_applied"].astype(str)
print(df_clean["days_since_applied"].dtype)

df_clean.to_csv("job_applications_updated.csv", index=False)

print("")
print("Stripping whitespace / fixing string formatting")
df_clean["company_name"] = df_clean["company_name"].str.strip()
df_clean["Current Status"] = df_clean["Current Status"].str.lower()

print("")
print("Grouping and Aggregating")
print(df_clean.groupby("Current Status").size())