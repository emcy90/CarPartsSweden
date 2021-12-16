from app.dll.repository import staffs_has_cps_orders_repository


def get_staff_has_cps_order_by_id():
    return staffs_has_cps_orders_repository.get_staff_has_cps_order_by_id()


def create_staff_has_cps_order(staff_has_cps_order):
    staffs_has_cps_orders_repository.create_staff_has_cps_order(staff_has_cps_order)


