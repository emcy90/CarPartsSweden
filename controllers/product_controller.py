from data.repository import product_repository


def get_product_by_id(_id):
    return product_repository.get_product_by_id(_id)


def create_product(product):
    product_repository.create_product(product)
