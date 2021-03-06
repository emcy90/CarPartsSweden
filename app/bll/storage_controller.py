from app.dll.repository import storage_repository


def get_storage_by_id():
    return storage_repository.get_storage_by_id()


def create_storage(storage):
    storage_repository.create_storage(storage)


def mongo_create_storage(super_storage):
    storage_repository.mongo_create_storage(super_storage)
