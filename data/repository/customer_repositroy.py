from data.db import session
from data.models import Customer


def get_customer_by_id(_id):
    return session.query(Customer).filter(Customer.id_customers == _id).first()


def create_customer(customer):
    customer = Customer(**customer)
    session.add(customer)
    session.commit()
