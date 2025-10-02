def increment(number, by=1):  # Optional parameters should be at end, first required one.
    return number + by


# Keyword Arguments
print(increment(number=2))
print(increment(number=2, by=2))
