from app.dll.db import session
from app.dll.models import OrderDetail


def get_order_details_by_id():
    details_id = session.query(OrderDetail.orders_order_no).all()
    order_details_id_clean_list = []
    for id in details_id:
        order_details_id_clean_list.append(id[0])
    return order_details_id_clean_list


def get_products_product_by_id():
    products_product = session.query(OrderDetail.products_product_id).all()
    products_product_by_id_clean_list = []
    for id in products_product:
        products_product_by_id_clean_list.append(id[0])
    return products_product_by_id_clean_list


def create_order_details(orderdetails):
    order_details = OrderDetail(**orderdetails)
    session.add(order_details)
    session.commit()
    print()
    print('Added orderdetails successfully!!')
