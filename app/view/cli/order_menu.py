from app.bll.order_controller import create_order, show_order
from app.view import main


def order_menu():
    running = True
    while running:
        print('========== Order Menu ==========')
        print()
        print("1. View order")
        print('2. Go back to main menu')

        input_choice = input("> ")
        if input_choice == "1":
            order_no = input("Order no: ")
            show_order(order_no)
            running = False

        elif input_choice == "2":
            running = False
            main()

        # elif input_choice == "2":
            # create_order()

