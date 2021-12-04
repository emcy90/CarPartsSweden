from data.db import session
from data.models import StaffHasCustomer


def get_staff_has_customer_by_id():
    staff_has_customer = session.query(StaffHasCustomer.staffs_id_staff).all()
    staff_has_customer_id_clean_list = []
    for id in staff_has_customer:
        staff_has_customer_id_clean_list.append(id[0])
    return staff_has_customer_id_clean_list


def create_staff_has_customer(staff_has_customer):
    staff_has_customer = StaffHasCustomer(**staff_has_customer)
    session.add(staff_has_customer)
    session.commit()
