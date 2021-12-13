from app.dll.db import session
from app.dll.models import Customer, Order


def get_records_by_name(_name):
    customer = session.query(Customer).filter(Customer.first_name == _name).all()
    customer_clean_list = []
    for no in customer:
        customer_clean_list.append(no)
    print(customer_clean_list)
    return customer_clean_list


def get_records_by_order_no(_order):
    order = session.query(Order).filter(Order.order_no == _order).all()
    order_clean_list = []
    for no in order:
        order_clean_list.append(no)
    print(order_clean_list)
    return order_clean_list


def get_all_records():
    pass
