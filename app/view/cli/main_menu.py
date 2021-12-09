def menu():
    print("*" * 50)
    print("Welcome to the APP")
    print("*" * 50)
    print()
    print("1. Customer menu")
    print("2. Show order")
    print("3. ")
    print("4. ")
    print("5. ")
    print()
    print("9. Quit")
    while True:
        pick = input("> ")
        if pick in "123459":
            break
        print("Valid options are 1, 2, 3, 4, 5 or 9")
    return pick
