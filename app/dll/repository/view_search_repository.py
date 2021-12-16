from app.dll.db import session
from app.dll.models import Storage, Product


def search_view_by_id(_id):
    storage_id_view = session.query(Storage).filter(Storage.storage_id == _id).first()
    return storage_id_view


def search_product_view_by_id(_id):
    product_id_view = session.query(Product).filter(Product.product_id == _id).first()
    return product_id_view
