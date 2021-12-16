from app.dll.db import session
from app.dll.models import Storage
from pymongo import MongoClient

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps


def get_storage_by_id():
    storage_id = session.query(Storage.storage_id).all()
    storage_id_clean_list = []
    for id in storage_id:
        storage_id_clean_list.append(id[0])
    return storage_id_clean_list


def create_storage(storage):
    storage = Storage(**storage)
    session.add(storage)
    session.commit()
    print()
    print('Added storage successfully!')


def mongo_create_storage(super_storage):
    my_clean_dict = super_storage
    print()
    db.storage.insert_one(my_clean_dict)
    print("Added mongo storage")
