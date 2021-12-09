from app.dll.db import session
from app.dll.models import Staff


def get_staff_by_id():
    staff_id = session.query(Staff.id_staff).all()
    staff_id_clean_list = []
    for id in staff_id:
        staff_id_clean_list.append(id[0])
    return staff_id_clean_list


def create_staff(staff):
    staff = Staff(**staff)
    session.add(staff)
    session.commit()
