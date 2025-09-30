# Ternary Operator
age = 22

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Cleaner Way
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# Much cleaner way
msg = "Eligible" if age >= 18 else "Not Eligible"
print(msg)
