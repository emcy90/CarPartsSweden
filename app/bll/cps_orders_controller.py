from app.dll.repository import cps_orders_repository


def get_cps_orders_by_id():
    return cps_orders_repository.get_cps_orders_by_id()


def create_cps_orders(cps_orders):
    cps_orders_repository.create_cps_orders(cps_orders)

def mongo_create_cps_orders(super_cps_orders):
    cps_orders_repository.mongo_create_cps_orders(super_cps_orders)

