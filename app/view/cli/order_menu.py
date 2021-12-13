from app.bll.order_controller import create_order, show_order


def order_menu():
    running = True
    while running:
        print('========== Order Menu ==========')
        print()
        print("1. View order")
        print('2. Create order')

        input_choice = input("> ")
        if input_choice == "1":
            order_no = input("Order no: ")
            show_order(order_no)
            running = False

        elif input_choice == "2":
            # create_order()
            pass
