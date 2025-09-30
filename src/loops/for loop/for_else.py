passed = True
successful = False

for number in range(3):
    print("Attempt", number)
    if passed:
        print("Attempt is Successful!")
        break

print()

# For Else Statement
for number in range(3):
    print("Attempt", number)
    if successful:
        print("Attempt is Successful!")
        break
else:
    print(f"Attempted 3 times but Failed!")
