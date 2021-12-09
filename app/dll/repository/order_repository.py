from app.dll.db import session
from app.dll.models import Order


def get_order_by_id():
    order_no = session.query(Order.order_no).all()
    order_no_clean_list = []
    for no in order_no:
        order_no_clean_list.append(no[0])
    return order_no_clean_list

    # WITH COMPREHENSION
    # order_id = session.query(Order.order_no).all()
    # order_no_clean_list = [no[0] for no in order_no]
    # return order_no_clean_list


def create_order(order):
    order = Order(**order)
    session.add(order)
    session.commit()
    print()
    print('Added order successfully!')
