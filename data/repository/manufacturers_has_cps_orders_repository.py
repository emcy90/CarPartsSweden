from data.db import session
from data.models import ManufacturerHasCpsOrder


def get_manufacturer_has_cps_order_by_id(_id):
    return session.query(ManufacturerHasCpsOrder)\
        .filter(ManufacturerHasCpsOrder.manufacturers_manufacturer_id == _id).first()


def create_manufacturer_has_cps_order(manufacturer_has_cps_order):
    manufacturer_has_cps_order = ManufacturerHasCpsOrder(**manufacturer_has_cps_order)
    session.add(manufacturer_has_cps_order)
    session.commit()

