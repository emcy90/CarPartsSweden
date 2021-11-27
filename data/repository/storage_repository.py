from data.db import session
from data.models import Storage


def get_storage_by_id(_id):
    return session.query(Storage).filter(Storage.storage_id == _id).first()


def create_storage(storage):
    storage = Storage(**storage)
    session.add(storage)
    session.commit()
