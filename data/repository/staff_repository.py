from data.db import session
from data.models import Staff


def get_staff_by_id(_id):
    return session.query(Staff).filter(Staff.id_staff == _id).first()


def create_staff(staff):
    staff = Staff(**staff)
    session.add(staff)
    session.commit()


