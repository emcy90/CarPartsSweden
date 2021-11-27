from data.db import session
from data.models import Supplier


def get_supplier_by_id(_id):
    return session.query(Supplier).filter(Supplier.supplier_id == _id).first()


def create_supplier(supplier):
    supplier = Supplier(**supplier)
    session.add(supplier)
    session.commit()

