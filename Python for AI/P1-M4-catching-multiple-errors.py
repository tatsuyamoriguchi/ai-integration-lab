try:
    # number = int("abc")
    number = 10 / 0
except ValueError:
    print("That wasn't a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")