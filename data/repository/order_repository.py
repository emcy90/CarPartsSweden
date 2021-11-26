from data.db import session
from data.models import Order


def get_order_by_id(_id):
    return session.query(Order).filter(Order.order_no == _id).first()


def create_order(order):
    order = Order(**order)
    session.add(order)
    session.commit()
