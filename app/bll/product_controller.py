from app.dll.repository import product_repository


def get_product_by_id():
    return product_repository.get_product_by_id()


def create_product(product):
    product_repository.create_product(product)


def mongo_create_product(super_product):
    product_repository.mongo_create_product(super_product)
