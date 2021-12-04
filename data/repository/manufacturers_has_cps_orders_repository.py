from data.db import session
from data.models import ManufacturerHasCpsOrder


def get_manufacturer_has_cps_order_by_id():
    manu_cps_id = session.query(ManufacturerHasCpsOrder.manufacturers_manufacturer_id).all()
    manufacturer_has_cps_order_id_clean_list = []
    for id in manu_cps_id:
        manufacturer_has_cps_order_id_clean_list.append(id[0])
    return manufacturer_has_cps_order_id_clean_list


def create_manufacturer_has_cps_order(manufacturer_has_cps_order):
    manufacturer_has_cps_order = ManufacturerHasCpsOrder(**manufacturer_has_cps_order)
    session.add(manufacturer_has_cps_order)
    session.commit()
