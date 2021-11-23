from data.db import session
from data.models import Manufacture


def get_manufacturer_by_id(_id):
    return session.query(Manufacture).filter(Manufacture.id_customers == _id).first()


def create_manufacture(manufacturers):
    manufacture = Manufacture(**manufacturers)
    session.add(manufacturers)
    session.commit()
