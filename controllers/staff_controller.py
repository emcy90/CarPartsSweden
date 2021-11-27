from data.repository import staff_repository


def get_customer_by_id(_id):
    return staff_repository.get_staff_by_id(_id)


def create_staff(staff):
    staff_repository.create_staff(staff)

