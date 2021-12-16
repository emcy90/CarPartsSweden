from app.dll.db import session
from app.dll.models import Product
from pymongo import MongoClient

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps

def get_product_by_id():
    product_id = session.query(Product.product_id).all()
    product_id_clean_list = []
    for id in product_id:
        product_id_clean_list.append(id[0])
    return product_id_clean_list


def create_product(product):
    product = Product(**product)
    session.add(product)
    session.commit()
    print()
    print('Added product successfully!')


def mongo_create_product(super_product):
    my_clean_dict = super_product
    print()
    db.products.insert_one(my_clean_dict)
    print("Added mongo product")
