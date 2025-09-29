# String Methods

course = "Python Programming"
course_space = "  Python Programming"

print(course)

print(f"Upper Case: {course.upper()}")  # This is new String, Original one not affected

print(f"Lower Case: {course.lower()}")

print(f"Capitalize: {course.capitalize()}")

print(f"Original String: {course}")

print(f"Title: {course.title()}")

print(f"Strip Space: {course_space.strip()}")  # lstrip(), rstrip()

print(f"Find: {course.find("Pro")}")  # Not found -1

print(f"Replace: {course.replace("P", "J")}")

print("Pro" in course)

print("Cool" not in course)
