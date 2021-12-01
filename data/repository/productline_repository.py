from data.db import session
from data.models import Productline


def get_productline_by_id(_id):
    return session.query(Productline).filter(Productline.productline == _id).first()


def create_productline(productline):
    productline = Productline(**productline)
    session.add(productline)
    session.commit()
    print()
    print('Added productline successfully!!!')
