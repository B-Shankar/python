# Formatted String

first_name = "Bhimashankar"
last_name = "Holkundi"

# Concatenation of Strings
full_name = first_name + " " + last_name
print(full_name)

print()

# f - formatted string literal - Prefix a String f or F + followed by double quotes + each value in parentheses + space if needed
complete_name = f"{first_name} {last_name}"
print(complete_name)

# formatted string: we can use any valid expression
user_details = f"\n\n{first_name} {last_name} \nAge: {len(full_name)} \nFav No: {5 + 2}"
print(user_details)
