def classify_experience(years):
    if years < 0:
        raise ValueError("Years cannnot be negative.")
    if years < 2:
        return "Junior"
    if years <= 5:
        return "Mid-level"
    else:
        return "Senior"

try:
    print(classify_experience(-1))
except ValueError as e:
    print(f"Invalid input: {e}")