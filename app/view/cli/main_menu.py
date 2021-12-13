def menu():
    print("*" * 50)
    print("Welcome to the APP")
    print("*" * 50)
    print()
    print("1. Customer menu")
    print("2. Order menu")
    print()
    print("9. Quit")
    while True:
        pick = input("> ")
        if pick in "129":
            break
        print("Valid options are 1, 2 or 9")
    return pick
