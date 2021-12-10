from app.dll.db import session
from app.dll.models import Customer, CustomerCar
# from app.view.cli.customer_menu import customer_menu
from app.view import main
from app.view.cli.main_menu import menu


# from app.view.cli.cli_app import main


def get_customer_by_id():
    # DELETE?
    # return session.query(Customer.id_customers).all()
    # return session.query(Order.order_no).all()
    # return session.query(Product.product_id).all()

    customer_id = session.query(Customer.id_customers).all()
    customer_id_clean_list = []
    for id in customer_id:
        customer_id_clean_list.append(id[0])
    return customer_id_clean_list


def show_all_customers():
    show_customers = session.query(Customer).all()
    count = 0
    for customers in show_customers:
        xc = len(customers.customer_cars)
        print(customers.customer_cars[count].color)
        if count == xc:
            count = 0
#        print(
 #           f'Customer id: {customers.customer_cars.color} First name: {customers.first_name} Last name: {customers.last_name}')

    # print(show_customers)
    # print()
    # print("*" * 50)
    # show_customers = session.query(Customer.id_customers).all()
    # show_cust = session.query(Customer.id_customers).all()
    # show_customers = []
    # for id in show_cust:
    #     show_customers.append(id[0])
    # for i in range(len(show_customers)):
    #     print(f'Customer id: {show_cust.id_customers}, First name: {show_customers.first_name},'
    #           f' Last name: {show_customers.last_name}, Company name: {show_customers.company_name},'
    #           f' Phone: {show_customers.phone}, Adress 2: {show_customers.product_description},'
    #           f' City: {show_customers.city}, Zipcode: {show_customers.zip_code},'
    #           f' Country: {show_customers.country}, sales_representant: {show_customers.sales_representant},'
    #           f' State: {show_customers.states}')
    #     print()
    #     print('*******************************************************************')


def delete_customer(xxx):
    del_customer2 = session.query(Customer).filter(Customer.id_customers == xxx).first()
    # staff = session.query(StaffHasStaff).filter(StaffHasStaff.staffs_id_staff == _id).first()
    print(del_customer2)
    # our_view_storage_and_product_view(delete_customer)
    # customer = customer_menu(del_customer)
    print(del_customer2.id_customers)
    print(f'Customer id: {del_customer2.id_customers}, First Name: {del_customer2.first_name},'
          f', Last Name: {del_customer2.last_name}, Company Name: {del_customer2.company_name},'
          f' Phone: {del_customer2.phone}, Address 1: {del_customer2.adress1},'
          f' Adress 2: {del_customer2.adress2}, City: {del_customer2.city},'
          f' Zip Code: {del_customer2.zip_code}, Country: {del_customer2.country},'
          f' Sales_representant: {del_customer2.sales_representant}, State: {del_customer2.states}')
    # print(data)
    xx = str(input("Do you want to delete this customer? Please type y for yes if you want to proceed "))

    if xx[0] == "y":
        session.query(Customer).filter(Customer.id_customers == xxx).delete()
        # session.query(CustomerCar).filter(CustomerCar.owner_id == xxx).delete
        session.commit()

    else:
        main()

    # print(f'Customer id: {customers.id_customers} First name: {customers.first_name} Last name: {customers.last_name}')


def create_customer(customer):
    customer = Customer(**customer)
    session.add(customer)
    session.commit()
    print()
    print('Added customer successfully.')
