# Access Index of a String

course_name = "Python Programming"

index_0 = course_name[0]  # P
index_1 = course_name[1]  # y
index_2 = course_name[-1]  # g
index_3 = course_name[-2]  # n

print(index_0)
print(index_1)
print(index_2)
print(index_3)

# [start:end]
print(f"First 3 Characters: {course_name[0:3]}")
print(f"First 15 Characters: {course_name[0:14]}")

# [start:] : No end then return full string
print(f"String with no end: {course_name[0:]}")

# [:end] : 0 to end
print(f"String with no start: {course_name[:3]}")

# [:] copy of original string
print(f"String with no start & end: {course_name[:]}")
