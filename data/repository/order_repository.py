from data.db import session
from data.models import Order


def get_order_by_id():
    return session.query(Order.order_no).all()


def create_order(order):
    order = Order(**order)
    session.add(order)
    session.commit()
    print()
    print('Added order successfully!')
