from data.db import session
from data.models import SupplierHasCpsOrder


def get_suppliers_has_cps_order_by_id(_id):
    return session.query(SupplierHasCpsOrder).filter(SupplierHasCpsOrder.suppliers_supplier_id == _id).first()



def create_suppliers_has_cps_order(supplier_has_cps_order):
    supplier_has_cps_order = SupplierHasCpsOrder(**supplier_has_cps_order)
    session.add(supplier_has_cps_order)
    session.commit()
