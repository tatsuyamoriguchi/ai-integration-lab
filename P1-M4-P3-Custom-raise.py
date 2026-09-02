# 3. Custom raise
# Update your classify_experience(years) function from Module 1 to raise 
# ValueError("Years cannot be negative") if years < 0. Wrap a call to it in a try/except 
# and test with classify_experience(-3).

# Module 1 function
# def classify_experience(years):

#     if years < 2:
#         print("Junior")
#     elif years <= 5:
#         print("Mid-level")
#     else:
#         print("Senior")

def classify_experience(years):

    if years < 0:
        raise ValueError("Years cannnot be negative.")
    elif years < 2:
        return "Junior"
    elif years <= 5:
        return "Mid-level"
    else:
        return "Senior"

try:
    print(classify_experience(3))
except ValueError as e:
    print(f"Invalid input: {e}")


