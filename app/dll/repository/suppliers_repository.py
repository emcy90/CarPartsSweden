from app.dll.db import session
from app.dll.models import Supplier


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
