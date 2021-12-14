from app.dll.db import session
from app.dll.models import Supplier
from pymongo import MongoClient

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps


def get_supplier_by_id():
    supplier_id = session.query(Supplier.supplier_id).all()
    supplier_id_clean_list = []
    for id in supplier_id:
        supplier_id_clean_list.append(id[0])
    return supplier_id_clean_list


def create_supplier(supplier):
    supplier = Supplier(**supplier)
    session.add(supplier)
    session.commit()
    print()
    print('Added supplier successfully!')


def mongo_create_supplier(super_supplier):
    my_clean_dict = super_supplier
    print()
    db.supplier.insert_one(my_clean_dict)
    print("Added mongo supplier")
