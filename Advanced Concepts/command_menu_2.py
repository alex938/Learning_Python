def start():
    return "System is starting..."

def stop():
    return "System is stopping..."

def restart():
    return "System is restarting..."

def status():
    return "System status: Running"

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

    action = commands.get(command, unknown_command)
    
    print(action())

menu()
