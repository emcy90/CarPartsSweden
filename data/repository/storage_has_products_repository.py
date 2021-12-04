from data.db import session
from data.models import StorageHasProducts


def get_storage_has_products_by_id():
    storage_product = session.query(StorageHasProducts.storage_storage_id).all()
    storage_has_products_id_clean_list = []
    for _id in storage_product:
        storage_has_products_id_clean_list.append(_id[0])
    return storage_has_products_id_clean_list


def create_storage_has_product(storage_has_product):
    storage_has_product = StorageHasProducts(**storage_has_product)
    session.add(storage_has_product)
    session.commit()
