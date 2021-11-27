from data.repository import suppliers_repository


def get_supplier_by_id(_id):
    return suppliers_repository.get_supplier_by_id(_id)


def create_supplier(supplier):
    suppliers_repository.create_supplier(supplier)

