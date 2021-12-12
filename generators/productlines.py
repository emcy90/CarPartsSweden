from app.dll.db import session
from app.dll.models import Productline


def get_productline_by_id():
    productline = session.query(Productline.product_description).all()
    productline_id_clean_list = []
    for id in productline:
        productline_id_clean_list.append(id[0])
    return productline_id_clean_list


def create_productline(productline):
    productline = Productline(**productline)
    session.add(productline)
    session.commit()
    print()
    print('Added productline successfully!!!')
