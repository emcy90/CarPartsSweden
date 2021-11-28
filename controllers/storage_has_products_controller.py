from data.repository import storage_has_products_repository


def get_storage_has_products_by_id(_id):
    return storage_has_products_repository.get_storage_has_products_by_id(_id)


def create_storage_has_product(storage_has_product):
    storage_has_products_repository.create_storage_has_product(storage_has_product)
