from data.db import session
from data.models import CpsOrder


def get_cps_orders_by_id():
    cps_order = session.query(CpsOrder.internal_order_no).all()
    cps_order_clean_list = []
    for no in cps_order:
        cps_order_clean_list.append(no[0])
    return cps_order_clean_list


def create_cps_orders(cps_orders):
    cps_orders = CpsOrder(**cps_orders)
    session.add(cps_orders)
    session.commit()
