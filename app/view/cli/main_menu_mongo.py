def mongo_menu():
    print("*" * 50)
    print("Welcome to MongoDB")
    print("*" * 50)
    print("(1) customers collection")
    print()
    print("(9) Quit")
    running = True
    while running:
        pick = ""
        pick = input("> ")
        if pick in "19":
            running = False

        return pick

