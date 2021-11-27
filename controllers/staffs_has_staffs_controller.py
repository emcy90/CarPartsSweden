from data.repository import staffs_has_staffs_repository


def get_staff_has_staff_by_id(_id):
    return staffs_has_staffs_repository.get_staff_has_staff_by_id(_id)


def create_staff_has_staff(staff_has_staff):
    staffs_has_staffs_repository.create_staff_has_staff(staff_has_staff)

