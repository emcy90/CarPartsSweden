from app.dll.db import session
from app.dll.models import Storage


def get_storage_by_id():
    storage_id = session.query(Storage.storage_id).all()
    storage_id_clean_list = []
    for id in storage_id:
        storage_id_clean_list.append(id[0])
    return storage_id_clean_list

    # WITH COMPREHENSION
    # storage_id = session.query(storage.storage_id).all()
    # storage_id_clean_list = [id[0] for id in storage_id]
    # return storage_id_clean_list


def create_storage(storage):
    storage = Storage(**storage)
    session.add(storage)
    session.commit()
    print()
    print('Added storage successfully!')