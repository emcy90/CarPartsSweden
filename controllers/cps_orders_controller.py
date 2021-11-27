from data.repository import cps_orders_repository


def get_cps_orders_by_id(_id):
    return cps_orders_repository.get_cps_orders_by_id(_id)


def create_cps_orders(cps_orders):
    cps_orders_repository.create_cps_orders(cps_orders)


