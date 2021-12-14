from app.dll.db import session
from app.dll.models import Staff
from pymongo import MongoClient

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps

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
    print()
    print('Added staff successfully!')


def mongo_create_staff(super_staff):
    my_clean_dict = super_staff
    print()
    db.staff.insert_one(my_clean_dict)
    print("Added mongo staff")
