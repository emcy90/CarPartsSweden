from app.dll.db import session
from app.dll.models import Customer


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
    show_customers = session.query(Customer.id_customers).all()




    print(f'Customer id: {show_customers.id_customers}, First name: {show_customers.first_name},'
            f' Last name: {show_customers.last_name}, Company name: {show_customers.company_name},'
            f' Phone: {produkten.product_id}, Adress 2: {produkten.product_description},'
            f' City: {show_customers.last_name}, Zipcode: {show_customers.company_name}',

          )

def create_customer(customer):
    customer = Customer(**customer)
    session.add(customer)
    session.commit()
    print()
    print('Added customer successfully.')
