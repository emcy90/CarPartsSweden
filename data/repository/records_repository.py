from data.db import session
from data.models import Customer, Order, StaffHasCustomer


def get_records_by_name(name):
    customer = session.query(Customer).filter_by(first_name=name).all()
    customer_clean_list = []
    for no in customer:
        customer_clean_list.append((no[0]))
    print(customer_clean_list)
    return customer_clean_list


def get_records_by_order_no(order):
    order = session.query(Order.order_no).filter.first()
    order_clean_list = []
    for no in order:
        order_clean_list.append(no[0])
    print(order_clean_list)
    return order_clean_list


def get_records_by_staff_has_customer():
    staff_has_customer = session.query(StaffHasCustomer.staffs_id_staff).filter.first()
    staff_has_customer_clean_list = []
    for no in staff_has_customer:
        staff_has_customer_clean_list.append(no[0])
    return staff_has_customer_clean_list


def show_records_by_order_no():
    #records = Records()
    #session.add(records)
    #session.commit()
    pass


def get_all_records():
    pass
