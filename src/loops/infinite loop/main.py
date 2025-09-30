while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "exit" or command.lower() == "quit":
        break
