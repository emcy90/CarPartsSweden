from app.bll.customer_controller import create_customer


def customer_menu():
    while True:
        print('Customer Menu')
        print()
        print("1. view customer")
        print('2. view all customers')
        print('3. add customer')

        input_choice = input("> ")
        if input_choice == "1":
            pass

        elif input_choice == "2":
            pass
            # customer = get_all_customers()  # skapa en funktion i controllern som pratar med customer repo som hämtar
            # # alla customers
            # for customer in customers:
            #     print(customer)

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

            create_single_customer = {first_name, last_name, company_name, phone, adress1, adress2, city, zip_code,
                                      country, sales_representant, states}

            # create_customer_dict(customer_key_list, create_single_customer):
            single_customer = dict(zip(customer_key_list, create_single_customer))

            create_customer(single_customer)
