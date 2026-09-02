# 2. Multiple except blocks
# Write a function that takes user input (as a string) and tries to convert it to an integer 
# using int(). Catch ValueError if the input isn't a valid number, and print an appropriate 
# message either way.

def convert(a):
    try:
        int_number = int(a)
        print(f"Convert was succesful, {a} converted to {int_number}")
    except ValueError:
        print(f"Input value, {a} isn't a valid number")

convert("2")
convert("abx")
