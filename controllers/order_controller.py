from data.repository import order_repository


def get_order_by_no(_id):
    return order_repository.get_order_by_id(_id)


def create_order(order):
    order_repository.create_order(order)
