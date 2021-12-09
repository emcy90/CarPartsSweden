from app.view.cli.customer_menu import customer_menu
from app.view.cli.main_menu import menu
from app.view.cli.records import *


def main():
    while True:
        menu_pick = menu()
        if menu_pick == "1":
            print("customer menu")
            customer_menu()
        elif menu_pick == "2":
            print("Show order")
            show_order()
            # show_all_customers()
        elif menu_pick == "4":
            print("fake order stuff")
            show_order()
        elif menu_pick == "5":
            print("pretend shit about seller")
        elif menu_pick == "9":
            break


if __name__ == '__main__':
    main()
