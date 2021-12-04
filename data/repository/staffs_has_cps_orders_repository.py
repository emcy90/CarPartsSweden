from data.db import session
from data.models import StaffHasCpsOrder


def get_staff_has_cps_order_by_id():
    staff_has_cps = session.query(StaffHasCpsOrder.staffs_id_staff).all()
    staff_has_cps_order_id_clean_list = []
    for _id in staff_has_cps:
        staff_has_cps_order_id_clean_list.append(_id[0])
    return staff_has_cps_order_id_clean_list


def create_staff_has_cps_order(staff_has_cps_order):
    staff_has_cps_order = StaffHasCpsOrder(**staff_has_cps_order)
    session.add(staff_has_cps_order)
    session.commit()
