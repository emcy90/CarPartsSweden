from app.dll.repository import customer_repository


def get_customer_by_id():
    return customer_repository.get_customer_by_id()


def show_all_customer():
    return customer_repository.show_all_customers()


def delete_customer(del_customer):
    return customer_repository.delete_customer(del_customer)


def create_customer(customer):
    customer_repository.create_customer(customer)


def mongo_create_customer(mongo_customer):
    return customer_repository.mongo_create_customer(mongo_customer)


def update_customer(customer):
    customer_repository.update_customer(customer)
