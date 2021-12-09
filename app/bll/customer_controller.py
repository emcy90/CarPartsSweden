from app.dll.repository import customer_repository


def get_customer_by_id():
    return customer_repository.get_customer_by_id()


def create_customer(customer):
    customer_repository.create_customer(customer)
