def menu():
    print("*" * 50)
    print("Welcome to the APP")
    print("*" * 50)
    print()
    print("1. Customer menu")
    print("2. Order menu")
    print()
    print("9. Quit")
    running = True
    while running:
        pick = input("> ")
        if pick in "129":
            running = False

        return pick
