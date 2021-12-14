from app.dll.repository import suppliers_repository


def get_supplier_by_id():
    return suppliers_repository.get_supplier_by_id()


def create_supplier(supplier):
    suppliers_repository.create_supplier(supplier)


def mongo_create_supplier(super_supplier):
    suppliers_repository.mongo_create_supplier(super_supplier)
