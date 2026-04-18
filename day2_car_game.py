op = True
while True:
 help = input(">>")
 help = help.lower()
 if help == "help":
    print('''
    +---------------------------------------------------+
    |  Welcome to the Car Game!                         |
    |  In this game, you will be driving a car.         |
    |  You can choose to start, stop, or quit           |
    |  Your goal is to reach your destination safely.   |
    +---------------------------------------------------+
    ''')
 while op:
   
    cmd = input("Enter a command (start/stop/quit): ")
    cmd = cmd.lower()
    if cmd == "start":
        print("Car started...🚗------- Let's go!")
    elif cmd == "stop":
        print("Car stopped [🚗].")
    elif cmd == "quit":
        print("Quitting the game. Goodbye!")
        op = False
    else:
        print("Invalid command. Please enter start, stop, or quit.")
   