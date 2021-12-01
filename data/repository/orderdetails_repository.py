from data.db import session
from data.models import OrderDetail


def get_order_details_by_id(_id):
    return session.query(OrderDetail).filter(OrderDetail.orders_order_no == _id).first()


def create_order_details(orderdetails):
    order_details = OrderDetail(**orderdetails)
    session.add(order_details)
    session.commit()
    print()
    print('Added orderdetails successfully!!')
