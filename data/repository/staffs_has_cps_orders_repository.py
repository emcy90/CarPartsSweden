from data.db import session
from data.models import StaffHasCpsOrder


def get_staff_has_cps_order_by_id(_id):
    return session.query(StaffHasCpsOrder).filter(StaffHasCpsOrder.id_staff == _id).first()


def create_staff_has_cps_order(staff_has_cps_order):
    staff_has_cps_order = StaffHasCpsOrder(**staff_has_cps_order)
    session.add(staff_has_cps_order)
    session.commit()

