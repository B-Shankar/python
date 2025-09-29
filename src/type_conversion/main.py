# Type Conversion
# str(), int(), float(), bool()

# type() - return the type of value passed
test = input()
print(type(test))

x = input("Enter a word: ")
print(f"x: {x}")

print()

a = input("Enter an integer: ")
num_word = "num_" + str(a)

print(f"num_word: {num_word}")
print(f"a: {a}")

print()

# bool() - Truthy, Falsy Values
# Falsy -> "", 0, None
# Truthy -> Other than ("", 0, None, like even, -1 , 5, 1 etc
print(bool(0))
print(bool(None))
print(bool(""))

print()

print(bool(-1))
print(bool(True))
print(bool(False))
