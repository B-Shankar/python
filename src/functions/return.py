# 1. Function that perform a task
# 2. Function that return a value

def get_greet(name):
    return f"Hello, {name}!"


message = get_greet("Bhimashankar")

print(message)
print(get_greet("Bhimashankar"))

# We can even write message to a file
file = open("file.txt", "w")
file.write(get_greet("Bhimashankar"))
file.close()
