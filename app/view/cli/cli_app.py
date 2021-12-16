from app.view.cli.customer_menu import customer_menu
from app.view.cli.main_menu import menu
from app.view.cli.order_menu import order_menu


def main():
    running = True
    while running:
        menu_pick = menu()
        if menu_pick == "1":
            print("customer menu")
            customer_menu()
        elif menu_pick == "2":
            print("order menu")
            order_menu()
            # show_all_customers()
        elif menu_pick == "9":
            running = False
            print("Quiting the app")


if __name__ == '__main__':
    main()
