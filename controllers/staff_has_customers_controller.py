from data.repository import staffs_has_customers_repository


def get_staff_has_customer_by_id(_id):
    return staffs_has_customers_repository.get_staff_has_customer_by_id(_id)


def create_customer(staff_has_customer):
    staffs_has_customers_repository.create_staff_has_customer(staff_has_customer)

