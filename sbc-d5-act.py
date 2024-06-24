commands = []
while True:
    command = input("COMMAND: ")
    if command.startswith("3"):
        num = command.split()[-1]
        commands.append(num)
        print(commands)
    elif command == "NAA":
        if commands:
            commands.pop(0)
        print(commands)
    elif command == "WALA":
        if commands:
            commands.pop()   
            print(commands) 
    elif command == "DISPLAY":
        print(commands)
    elif command == "QUIT":
        break    
    else:
        commands.append(command)
        print(commands)