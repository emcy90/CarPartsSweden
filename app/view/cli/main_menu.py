def menu():
    print("*" * 50)
    print("Welcome to the APP")
    print("*" * 50)
    print()
    print("1. Add customer")
    print("2. Show Customer")
    print("3. Delete Customer")
    print("4. Show order")
    print("5. show seller")
    print()
    print("9. Quit")
    while True:
        pick = input("> ")
        if pick in "123459":
            break
        print("Valid options are 1, 2, 3, 4, 5 or 9")
    return pick


def customer_menu():
    pass
