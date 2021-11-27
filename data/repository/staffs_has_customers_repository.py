from data.db import session
from data.models import StaffHasCustomer


def get_staff_has_customer_by_id(_id):
    return session.query(StaffHasCustomer).filter(StaffHasCustomer.staffs_id_staff == _id).first()


def create_staff_has_customer(staff_has_customer):
    staff_has_customer = StaffHasCustomer(**staff_has_customer)
    session.add(staff_has_customer)
    session.commit()

