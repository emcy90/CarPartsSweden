from app.dll.db import session
from app.dll.models import SupplierHasCpsOrder


def get_suppliers_has_cps_order_by_id():
    supplier_cps = session.query(SupplierHasCpsOrder.suppliers_supplier_id).all()
    suppliers_has_cps_order_id_clean_list = []
    for id in supplier_cps:
        suppliers_has_cps_order_id_clean_list.append(id[0])

    return suppliers_has_cps_order_id_clean_list


def get_suppliers_cps_orders_internal_order_no():
    supplier_internal = session.query(SupplierHasCpsOrder.cps_orders_internal_order_no).all()
    suppliers_cps_orders_internal_order_no_clean_list = []
    for no in supplier_internal:
        suppliers_cps_orders_internal_order_no_clean_list.append(no[0])

    return suppliers_cps_orders_internal_order_no_clean_list


def cps_orders_internal_order_no():
    supplier_cps = session.query(SupplierHasCpsOrder.cps_orders_internal_order_no).all()
    cps_orders_internal_order_no_clean_list = []
    for no in supplier_cps:
        cps_orders_internal_order_no_clean_list.append(no[0])

    return cps_orders_internal_order_no_clean_list


def create_suppliers_has_cps_order(supplier_has_cps_order):
    supplier_has_cps_order = SupplierHasCpsOrder(**supplier_has_cps_order)
    session.add(supplier_has_cps_order)
    session.commit()
    print()
    print('Added supplier has cps order successfully!')
