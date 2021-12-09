from app.dll.repository import order_repository


def get_order_by_no():
    return order_repository.get_order_by_id()


def create_order(order):
    order_repository.create_order(order)
