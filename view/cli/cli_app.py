from view.cli.main_menu import menu
from view.cli.records import *
from controllers.customer_controller import create_customer


def main():
    while True:
        menu_pick = menu()
        if menu_pick == "1":
            create_customer()
        elif menu_pick == "2":
            pass
        elif menu_pick == "3":
            get_records_by_order_no()
        elif menu_pick == "9":
            break


if __name__ == '__main__':
    main()
