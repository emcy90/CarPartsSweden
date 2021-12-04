from data.db import session
from data.models import Manufacture


def get_manufacturer_by_id():
    manu_id = session.query(Manufacture.manufacturer_id).all()
    manufacturer_id_clean_list = []
    for id in manu_id:
        manufacturer_id_clean_list.append(id[0])
    return manufacturer_id_clean_list


def create_manufacture(manufacturers):
    manufacture = Manufacture(**manufacturers)
    session.add(manufacture)
    session.commit()
