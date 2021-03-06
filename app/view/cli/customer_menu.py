from app.bll.customer_controller import create_customer, show_all_customer, delete_customer, update_customer, \
    show_one_customer
from app.view import main
from app.view.cli.main_menu import menu


def customer_menu():
    running = True
    while running:

        print('========== Customer Menu ==========')
        print()
        print("1. View customer")
        print('2. View all customers')
        print('3. Add customer')
        print('4. Delete customer')
        print('5. Update customer')
        print('6. Go back to main menu')
        # print('5. Go back to main menu')

        input_choice = str(input("> "))
        if input_choice == "1":
            xxx = int(input("Which customer do you want to view? "))
            show_one_customer(xxx)
            running = False

        elif input_choice == "2":
            show_all_customer()
            # customer = get_all_customers()  # skapa en funktion i controllern som pratar med customer repo som hämtar
            # # alla customers
            # for customer in customers:
            #     print(customer)
            running = False

        elif input_choice == "3":
            first_name = str(input("First Name: "))
            last_name = str(input("Last name: "))
            company_name = input("Company Name: ")
            phone = str(input("Phone: "))
            adress1 = str(input("Adress: "))
            adress2 = str(input("Adress2: "))
            city = str(input("City: "))
            zip_code = str(input("Zip Code: "))
            country = str(input("Country: "))
            sales_representant = str(input("Sales Representant: "))
            states = str(input("State: "))

            customer_key_list = ['first_name', 'last_name', 'company_name', 'phone', 'adress1', 'adress2',
                                 'city', 'zip_code', 'country', 'sales_representant', 'states']

            create_single_customer = [first_name, last_name, company_name, phone, adress1, adress2, city, zip_code,
                                      country, sales_representant, states]

            # create_customer_dict(customer_key_list, create_single_customer):
            single_customer = dict(zip(customer_key_list, create_single_customer))

            create_customer(single_customer)
            running = False

        elif input_choice == "4":
            del_customer = input("Delete customer by ID: ")
            # customer = str(input(f"Are you sure you want to delete {}?"))
            delete_customer(del_customer)
            running = False

        elif input_choice == "5":
            up_customer = input("Which customer do you want to update? ")
            update_customer(up_customer)
            print(f'Customer updated: updated')
            running = False

        elif input_choice == "6":
            running = False
            main()
