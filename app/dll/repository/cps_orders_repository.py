from app.dll.db import session
from app.dll.models import CpsOrder
from pymongo import MongoClient

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps


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
    print()
    print('Added cps order successfully!')
