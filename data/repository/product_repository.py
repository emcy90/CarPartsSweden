from data.db import session
from data.models import Product


def get_product_by_id():
    product_id = session.query(Product.product_id).all()
    product_id_clean_list = []
    for id in product_id:
        product_id_clean_list.append(id[0])
    return product_id_clean_list

    # WITH COMPREHENSION
    # product_id = session.query(Product.product_id).all()
    # product_id_clean_list = [id[0] for id in product_id]
    # return product_id_clean_list


def create_product(product):
    product = Product(**product)
    session.add(product)
    session.commit()
