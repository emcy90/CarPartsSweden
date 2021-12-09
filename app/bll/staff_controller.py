from app.dll.repository import staff_repository


def get_customer_by_id():
    return staff_repository.get_staff_by_id()


def create_staff(staff):
    staff_repository.create_staff(staff)

