from app.dll.db import session
from app.dll.models import StaffHasCpsOrder


def get_staff_has_cps_order_by_id():
    staff_has_cps = session.query(StaffHasCpsOrder.staffs_id_staff).all()
    staff_has_cps_order_id_clean_list = []
    for _id in staff_has_cps:
        staff_has_cps_order_id_clean_list.append(_id[0])
    return staff_has_cps_order_id_clean_list


def get_staffs_cps_orders_internal_order_no():
    staff_has_cps = session.query(StaffHasCpsOrder.cps_orders_internal_order_no).all()
    staffs_cps_orders_internal_order_no_clean_list = []
    for no in staff_has_cps:
        staffs_cps_orders_internal_order_no_clean_list.append(no[0])
    return staffs_cps_orders_internal_order_no_clean_list


def create_staff_has_cps_order(staff_has_cps_order):
    staff_has_cps_order = StaffHasCpsOrder(**staff_has_cps_order)
    session.add(staff_has_cps_order)
    session.commit()
    print()
    print('Added staff has cps order successfully!')
