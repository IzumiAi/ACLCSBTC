commands = []
while True:
    command = input("COMMAND: ")
    if command.startswith("0"):
        print(commands)
    elif command == "NAA":
        if commands:
            commands.pop(0)
        print(commands)
    elif command == "WALA":
        if commands:
            commands.pop()   
            print(commands) 
    elif command == "QUIT":
        break    
    else:
        commands.append(command)
        print(commands)