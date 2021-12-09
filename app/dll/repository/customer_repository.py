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

    # WITH COMPREHENSION
    # customer_id = session.query(Customer.id_customers).all()
    # customer_id_clean_list = [id[0] for id in customer_id]
    # return customer_id_clean_list


def create_customer(customer):
    customer = Customer(**customer)
    session.add(customer)
    session.commit()
    print()
    print('Added customer successfully.')
