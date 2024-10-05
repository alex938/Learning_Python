def start(message):
    return f"System is starting: {message}"

def stop():
    return "System is stopping..."

def restart():
    return "System is restarting..."

def status(info):
    return f"System status: {info}"

def unknown_command():
    return "Unknown command"

def menu():
    commands = {
        'start': start,
        'stop': stop,
        'restart': restart,
        'status': status
    }

    command = input("Enter a command (start/stop/restart/status): ").lower()

    if command == 'start':
        message = input("Enter a start message: ")
        action = commands.get(command, unknown_command)
        print(action(message))  

    elif command == 'status':
        info = "Running smoothly"
        action = commands.get(command, unknown_command)
        print(action(info))

    else:
        action = commands.get(command, unknown_command)
        print(action())

menu()
