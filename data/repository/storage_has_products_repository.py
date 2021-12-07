from data.db import session
from data.models import StorageHasProducts


def get_storage_has_products_by_id():
    storage_product = session.query(StorageHasProducts.storage_storage_id).all()
    storage_has_products_id_clean_list = []
    for _id in storage_product:
        storage_has_products_id_clean_list.append(_id[0])
    return storage_has_products_id_clean_list


def get_storage_products_product_by_id():
    products_product = session.query(StorageHasProducts.products_product_id).all()
    products_product_by_id_clean_list = []
    for _id in products_product:
        products_product_by_id_clean_list.append(_id[0])
    return products_product_by_id_clean_list


def create_storage_has_product(storage_has_product):
    storage_has_product = StorageHasProducts(**storage_has_product)
    session.add(storage_has_product)
    session.commit()
