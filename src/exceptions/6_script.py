x = 2

try:
    if not type(x) is str:
        # raise TypeError()
        raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Don't divide by zero")
except Exception as error:
    print(error)  # Only strings are allowed.
else:
    print("No errors occurred.")
finally:
    print("This will always execute.")
