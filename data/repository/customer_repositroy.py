from data.db import session
from data.models import Customer, Order


def get_customer_by_id():
    return session.query(Customer.id_customers).all()
    # return session.query(Order.order_no).all()
    # return session.query(Product.product_id).all()


def create_customer(customer):
    customer = Customer(**customer)
    session.add(customer)
    session.commit()
    print()
    print('Added customer successfully.')
