# For Loop

# range(count)
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

print()

# range(From, Before)
for number in range(1, 4):
    print("Attempt", number, number * ".")

print()

# range(From, Before, Step)
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
