# 1. Basic try/except
# Write a function safe_divide(a, b) that divides a by b, but catches ZeroDivisionError 
# and returns/prints a friendly message instead of crashing. Test it with safe_divide(10, 0) 
# and safe_divide(10, 2).

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")

safe_divide(3, 0)
safe_divide(2, 4)

        
