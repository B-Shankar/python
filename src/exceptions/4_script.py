# ZeroDivisionError

# ZeroDivisionError: division by zero, this is not caught above, because it is not a NameError
# x = 10
# try:
#     print(x / 0)
# except NameError:
#     print("NameError means something is probably undefined.")


# Solution: add another except block
x = 10
try:
    print(x / 0)
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Don't divide by zero")
