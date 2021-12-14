from app.dll.db import session
from app.dll.models import Order
from pymongo import MongoClient
from app.view import main

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps


def get_order_by_id():
    order_no = session.query(Order.order_no).all()
    order_no_clean_list = []
    for no in order_no:
        order_no_clean_list.append(no[0])
    return order_no_clean_list

    # WITH COMPREHENSION
    # order_id = session.query(Order.order_no).all()
    # order_no_clean_list = [no[0] for no in order_no]
    # return order_no_clean_list


def create_order(order):
    order = Order(**order)
    session.add(order)
    session.commit()
    print()
    print('Added order successfully!')


def mongo_create_order(super_order):
    my_clean_dict = super_order
    # customer = Customer(**customer)
    print()
    db.orders.insert_one(my_clean_dict)
    print("Added mongo order")


def show_order(xxx):
    order1 = session.query(Order).filter(Order.order_no == xxx).first()
    # staff = session.query(StaffHasStaff).filter(StaffHasStaff.staffs_id_staff == _id).first()
    print(order1)
    # our_view_storage_and_product_view(delete_customer)
    # customer = customer_menu(del_customer)
    print(order1.order_no)
    print(f'Order no: {order1.order_no}, Order date: {order1.order_date},'
          f' Required date: {order1.required_date}, Shipping_date: {order1.shipping_date},'
          f' Status: {order1.status}, Comments: {order1.comments}, Customer ID: {order1.customers_id_customers}')
    # print(data)
