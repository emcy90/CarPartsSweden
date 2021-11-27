from data.repository import storage_repository


def get_storage_by_id(_id):
    return storage_repository.get_storage_by_id(_id)


def create_storage(storage):
    storage_repository.create_storage(storage)

