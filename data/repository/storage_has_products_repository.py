from data.db import session
from data.models import StorageHasProducts


def get_storage_has_products_by_id(_id):
    return session.query(StorageHasProducts).filter(StorageHasProducts.storage_id == _id).first()


def create_storage_has_product(storage_has_product):
    storage_has_product = StorageHasProducts(**storage_has_product)
    session.add(storage_has_product)
    session.commit()
