from data.db import session
from data.models import StaffHasCpsOrder, Storage, StorageHasProducts, Product


def search_view_by_id(_id):
    # storage_object = []
    storage_id_view = session.query(Storage).filter(Storage.storage_id == _id).first()
    #    staff session.query(StaffHasStaff).filter(StaffHasStaff.staffs_id_staff == _id).first()
    # storage_object.append(storage_id_view)
    # return storage_object
    return storage_id_view


def search_product_view_by_id(_id):
    product_id_view = session.query(Product).filter(Product.product_id == _id).first()
    return product_id_view


    # staff_has_cps_order_id_clean_list = []
    # for _id in staff_has_cps:
    #    staff_has_cps_order_id_clean_list.append(_id[0])
    # return staff_has_cps_order_id_clean_list