from data.db import session
from data.models import StaffHasCustomer


def get_staff_has_customer_by_id():
    staff_has_customer = session.query(StaffHasCustomer.staffs_id_staff).all()
    staff_has_customer_id_clean_list = []
    for id in staff_has_customer:
        staff_has_customer_id_clean_list.append(id[0])
    return staff_has_customer_id_clean_list


def get_staffs_id_staffs():
    staff_has_customer = session.query(StaffHasCustomer.staffs_id_staff).all()
    staffs_id_staff_list = []
    for id in staff_has_customer:
        staffs_id_staff_list.append(id[0])
    return staffs_id_staff_list


def get_customers_id_customers_by_id():
    customers_id_customers = session.query(StaffHasCustomer.customers_id_customers).all()
    customers_id_customers_id_clean_list = []
    for no in customers_id_customers:
        customers_id_customers_id_clean_list.append(no[0])
    return customers_id_customers_id_clean_list


def create_staff_has_customer(staff_has_customer):
    staff_has_customer = StaffHasCustomer(**staff_has_customer)
    session.add(staff_has_customer)
    session.commit()
