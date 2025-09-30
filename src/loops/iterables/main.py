# In python as we have primitives type like int, bool, float, complex. But we have also Complex types like 'range' etc
print(type(5))  # type: 'int'
print(type(range(5)))  # type: 'range'

# range() is Iterable; it return the element that are iterable.
# Similarly, String, List are also iterable
for x in range(5):
    print(x)

print()

for s in "Python":
    print(s)

print()

for a in list(range(5)):
    print(a)
# or
for a in [10, 22, 35, 52, 56]:
    print(a)
