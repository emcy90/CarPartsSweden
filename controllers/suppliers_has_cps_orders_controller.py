from data.repository import suppliers_has_cps_orders_repository


def get_suppliers_has_cps_orders_by_id(_id):
    return suppliers_has_cps_orders_repository.get_suppliers_has_cps_order_by_id(_id)


def create_suppliers_has_cps_order(suppliers_has_cps_order):
    suppliers_has_cps_orders_repository.create_suppliers_has_cps_order(suppliers_has_cps_order)
