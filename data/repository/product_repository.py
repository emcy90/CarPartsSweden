from data.db import session
from data.models import Product


def get_product_by_id():
    return session.query(Product.product_id).all()


def create_product(product):
    product = Product(**product)
    session.add(product)
    session.commit()
