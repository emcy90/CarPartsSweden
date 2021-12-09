from app.dll.repository import orderdetails_repository


def get_order_details_by_id():
    return orderdetails_repository.get_order_details_by_id()


def create_order_details(orderdetails):
    orderdetails_repository.create_order_details(orderdetails)
