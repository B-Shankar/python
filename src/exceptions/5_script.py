x = 2

try:
    # print(x / 0)
    print(x / 2)
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Don't divide by zero")
else:
    print("No errors occurred.")
finally:
    print("This will always execute.")
