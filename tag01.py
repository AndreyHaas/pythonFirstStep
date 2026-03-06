print("Driver application\n")

isStarted = False

while True:
    command = input("> ").strip().lower()

    if command == "start":
        if not isStarted:
            print("Car started... Ready to go!")
            isStarted = True
        else:
            print("the car is started...")
    elif command == "stop":
        if isStarted:
            print("Car stopped...")
            isStarted = False
        else:
            print("the car is stopped...")
    elif command == "help" or command == "?":
        print('''
start   - to start the car
stop    - to stop the car
help/?  - to show this help
quit    - to exit the application
        ''')
    elif command == "quit":
        print("Got out of the car... Program was stopped!")
        break
    else:
        print("I don't understand that...")
