# Write a function classify_experience(years) that takes a number and prints:
# * "Junior" if under 2 years
# * "Mid-level" if 2–5 years
# * "Senior" if over 5 years
# Test it with classify_experience(5).

def classify_experience(years):

    if years < 2:
        print("Junior")
    elif years <= 5:
        print("Mid-level")
    else:
        print("Senior")

classify_experience(6)
