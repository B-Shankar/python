def all_number(*numbers):
    for number in numbers:
        print(number)


all_number(2, 3, 4, 5)

print()


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


value = multiply(2, 3, 4, 5)
print(value)
