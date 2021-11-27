from data.db import session
from data.models import StaffHasStaff


def get_staff_has_staff_by_id(_id):
    return session.query(StaffHasStaff).filter(StaffHasStaff.staffs_id_staff == _id).first()


def create_staff_has_staff(staff_has_staff):
    staff_has_staff = StaffHasStaff(**staff_has_staff)
    session.add(staff_has_staff)
    session.commit()
