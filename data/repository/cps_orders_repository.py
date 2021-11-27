from data.db import session
from data.models import CpsOrder


def get_cps_orders_by_id(_id):
    return session.query(CpsOrder).filter(CpsOrder.internal_order_no == _id).first()


def create_cps_orders(cps_orders):
    cps_orders = CpsOrder(**cps_orders)
    session.add(cps_orders)
    session.commit()
