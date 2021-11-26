from data.db import session
from data.models import Product


def get_product_by_id(_id):
    return session.query(Product).filter(Product.product_id == _id).first()


def create_product(product):
    product = Product(**product)
    session.add(product)
    session.commit()
