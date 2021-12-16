import time

from app.bll.cps_orders_controller import create_cps_orders, get_cps_orders_by_id
# from app.bll import create_car, get_customer_cars_by_reg_no
from app.bll.customer_controller import create_customer
from app.bll.manufacturer_controller import create_manufacture, get_manufacturer_by_id
from app.bll.manufacturers_has_cps_orders_controller import create_manufacturer_has_cps_order, \
    get_manufacturer_has_cps_order_by_id
from app.bll.order_controller import create_order
from app.bll.customer_car_controller import get_customer_cars_by_reg_no, create_car
from app.bll.orderdetails_controller import create_order_details, get_order_details_by_id
from app.bll.payment_controller import create_payment, get_payment_by_no
from app.bll.product_controller import get_product_by_id, create_product
from app.bll.productline_controller import create_productline, get_productline_by_id
from app.bll.staff_controller import create_staff
from app.bll.staff_has_customers_controller import create_staff_has_customer, get_staff_has_customer_by_id
from app.bll.staffs_has_cps_orders_controller import create_staff_has_cps_order, get_staff_has_cps_order_by_id
from app.bll.storage_controller import create_storage, get_storage_by_id
from app.bll.storage_has_products_controller import create_storage_has_product, get_storage_has_products_by_id
from app.bll.supplier_controller import create_supplier, get_supplier_by_id
from app.bll.suppliers_has_cps_orders_controller import create_suppliers_has_cps_order
from app.dll.repository.customer_repository import get_customer_by_id
# from app.dll. import get_order_by_id
# from app.dll import get_staff_by_id
# from app.dll import get_suppliers_has_cps_order_by_id
from app.dll.repository.order_repository import get_order_by_id
from app.dll.repository.staff_repository import get_staff_by_id
from app.dll.repository.suppliers_has_cps_orders_repository import get_suppliers_has_cps_order_by_id

from generators.cps_object import CpsCreator

# CREATING THE CREATOR OBJECT THAT HOLDS ALL INFO WE NEED TO CREATE OUR FAKE DATA.
creator = CpsCreator()
creator.load_all_data()

all_cps_order_ids = get_cps_orders_by_id()
all_cars_ids = get_customer_cars_by_reg_no()
all_customers_ids = get_customer_by_id()
all_order_no = get_order_by_id()
all_product_ids = get_product_by_id()
all_payments_ids = get_payment_by_no()
all_manufacturer_ids = get_manufacturer_by_id()
all_manufacturer_cps_order_ids = get_manufacturer_has_cps_order_by_id()
all_orderdetail_ids = get_order_details_by_id()
all_productline_ids = get_productline_by_id()
all_staff_ids = get_staff_by_id()
all_staffs_cps_order_ids = get_staff_has_cps_order_by_id()
all_staffs_has_customers_ids = get_staff_has_customer_by_id()
all_storage_has_products_ids = get_storage_has_products_by_id()
all_storage_ids = get_storage_by_id()
all_supplier_cps_orders_ids = get_suppliers_has_cps_order_by_id()
all_supplier_ids = get_supplier_by_id()
all_cps_order_internal_nos = get_cps_orders_by_id()

print(f'All customers id: {all_customers_ids}')
print(f'All cars ids: {all_cars_ids}')
print(f'All payment ids: {all_payments_ids}')
print(f'All order ids: {all_order_no}')
print(f'All product ids: {all_product_ids}')
print(f'All cps order ids: {all_cps_order_ids}')
print(f'All manufacturer ids: {all_manufacturer_ids}')
print(f'All manufacturer cps order ids: {all_manufacturer_cps_order_ids}')
print(f'All orderdetail ids: {all_orderdetail_ids}')
print(f'All productline ids: {all_productline_ids}')
print(f'All staff ids: {all_staff_ids}')
print(f'All staffs cps order ids: {all_staffs_cps_order_ids}')
print(f'All staffs has customer ids: {all_staffs_has_customers_ids}')
print(f'All storage has product ids: {all_storage_has_products_ids}')
print(f'All storage ids: {all_storage_ids}')
print(f'All supplier_cps_order ids: {all_supplier_cps_orders_ids}')
print(f'All supplier ids: {all_supplier_ids}')
print()

i = 79
for i in range(10):

    time.sleep(0.5)
    # CREATING A CUSTOMER OBJECT
    creator.assemble_customer_object()
    creator.customer_list = [creator.first_name, creator.last_name, creator.company, creator.phone,
                             creator.street_adress + " " + creator.house_number, '', creator.city, creator.zip_code,
                             creator.country, creator.my_sales_representant, creator.state]
    creator.create_customer_dict(creator.customer_key_list, creator.customer_list)
    # mg = creator.create_customer_dict(creator.customer_key_list, creator.customer_list)
    # print(creator.customer)
    create_customer(creator.customer)

    # CREATING A CAR OBJECT
    creator.assemble_car_object(all_cars_ids)
    customer_car_list = [creator.reg_no, creator.manufacturer, creator.color, creator.model,
                         creator.year_model, creator.owner_id]
    creator.create_customer_car_dict(creator.customer_car_key_list, customer_car_list)
    # print(creator.customer_car)
    create_car(creator.customer_car)

    # CREATING A PAYMENT OBJECT
    creator.assemble_payment_object()
    creator.payment_list = [creator.payment_date, creator.payment_amount, creator.customer_paid_bill_id]
    creator.create_payment_dict(creator.payment_key_list, creator.payment_list)
    # print(creator.payment)
    create_payment(creator.payment)

    # CREATING ORDER OBJECT
    creator.assemble_order_object()
    creator.order_list = [creator.order_date, creator.required_date, creator.shipping_date,
                          creator.status, creator.comments, creator.customers_id_customers]
    creator.create_order_dict(creator.order_key_list, creator.order_list)
    # print(creator.order)
    create_order(creator.order)

    # CREATING PRODUCTS OBJECT
    creator.assemble_products_object()
    creator.products_list = [creator.product_name, creator.product_description, creator.inprice,
                             creator.outprice]
    creator.create_product_dict(creator.product_key_list, creator.products_list)
    # print(creator.product)
    create_product(creator.product)

    # CREATING PRODUCTLINES OBJECT
    # This needs a productline.txt file, text_description.txt and html_description.txt
    # and image.txt to work, haven't got those files yet.
    creator.assemble_productline_object()
    creator.productline_list = [creator.product_description, creator.text_description, creator.html_description,
                                creator.image, creator.products_description_id]
    creator.create_productline_dict(creator.productline_key_list, creator.productline_list)
    # print(creator.productline)
    create_productline(creator.productline)

    # CREATING ORDERDETAILS OBJECT
    creator.assemble_orderdetails_object()
    creator.orderdetails_list = [creator.orders_order_no, creator.products_product_id, creator.quantity,
                                 creator.price_each]
    creator.create_orderdetails_dict(creator.orderdetails_key_list, creator.orderdetails_list)
    # print(creator.orderdetails)
    create_order_details(creator.orderdetails)

    # CREATING STORAGE OBJECT
    creator.assemble_storage_object()
    creator.storage_list = [creator.storage_name, creator.storage_quantity, creator.storage_city]
    creator.create_storage_dict(creator.storage_key_list, creator.storage_list)
    # print(creator.storage)
    create_storage(creator.storage)

    # CREATING STORAGE HAS PRODUCTS OBJECT
    creator.assemble_storage_has_products_object()
    creator.storage_has_products_list = [creator.storage_storage_id, creator.products_product_id]
    creator.create_storage_has_products_dict(creator.storage_has_products_key_list, creator.storage_has_products_list)
    # print(creator.storage_has_products)
    create_storage_has_product(creator.storage_has_products)

    # CREATING SUPPLIERS OBJECT
    creator.assemble_supplier_object()
    creator.supplier_list = [creator.supplier_name, creator.supplier_adress1, creator.supplier_adress2, creator.city,
                             creator.zip_code, creator.country, creator.suppliers_contact_person, creator.phone_number,
                             creator.email]
    creator.create_suppliers_dict(creator.suppliers_key_list, creator.supplier_list)
    # print(creator.suppliers)
    create_supplier(creator.suppliers)

    # CREATING CPS ORDERS OBJECT
    creator.assemble_cps_orders_object()
    creator.cps_orders_list = [creator.order_date, creator.required_date, creator.shipping_date,
                               creator.status, creator.comments, creator.order_no_comments]
    creator.create_cps_orders_dict(creator.cps_orders_key_list, creator.cps_orders_list)
    # print(creator.cps_orders)
    create_cps_orders(creator.cps_orders)

    # CREATING SUPPLIERS HAS CPS ORDERS OBJECT
    creator.assemble_suppliers_has_cps_orders_object()
    creator.suppliers_has_cps_orders_list = [creator.suppliers_supplier_id, creator.cps_orders_internal_order_no]
    creator.create_suppliers_has_cps_orders_dict(creator.suppliers_has_cps_orders_key_list,
                                                 creator.suppliers_has_cps_orders_list)
    # print(creator.suppliers_has_cps_orders)
    create_suppliers_has_cps_order(creator.suppliers_has_cps_orders)

    # CREATING MANUFACTURERS OBJECT
    creator.assemble_manufacturers_object()
    creator.manufacturers_list = [creator.name_manufacturer, creator.main_office_adress1,
                                  creator.main_office_adress2, creator.main_office_name,
                                  creator.manufacturer_contact_person, creator.contact_person_phone,
                                  creator.contact_person_email]
    creator.create_manufacturers_dict(creator.manufacturers_key_list, creator.manufacturers_list)
    # print(creator.manufacturers)
    create_manufacture(creator.manufacturers)

    # CREATING MANUFACTURERS HAS CPS ORDERS OBJECT
    creator.assemble_manufacturers_has_cps_orders_object()
    creator.manufacturers_has_cps_orders_list = [creator.manufacturers_manufacturer_id,
                                                 creator.cps_orders_internal_order_no]

    creator.create_manufactureres_has_cps_orders_dict(creator.manufacturers_has_cps_orders_key_list,
                                                      creator.manufacturers_has_cps_orders_list)
    # print(creator.manufactureres_has_cps_orders)
    create_manufacturer_has_cps_order(creator.manufactureres_has_cps_orders)  # manufacturers_has_cps_orders)

    # CREATING STAFFS OBJECT
    creator.assemble_staffs_object()
    creator.staffs_list = [creator.first_name, creator.last_name, creator.job_title,
                           creator.phone, creator.store, creator.reports_to]
    creator.create_staffs_dict(creator.staffs_key_list, creator.staffs_list)
    # print(creator.staffs)
    create_staff(creator.staffs)

    # CREATING STAFFS HAS CPS ORDERS OBJECT
    creator.assemble_staffs_has_cps_orders_object()
    creator.staffs_has_cps_orders_list = [creator.staffs_id_staff, creator.cps_orders_internal_order_no]
    creator.create_staffs_has_cps_orders_dict(creator.staffs_has_cps_orders_key_list,
                                              creator.staffs_has_cps_orders_list)
    # print(creator.staffs_has_cpsorders)
    create_staff_has_cps_order(creator.staffs_has_cpsorders)

    # CREATING STAFFS HAS CUSTOMERS OBJECT
    creator.assemble_staffs_has_customers_object()
    creator.staffs_has_customers_list = [creator.staffs_id_staff, creator.customers_id_customers]
    creator.create_staffs_has_customers_dict(creator.staffs_has_customers_key_list, creator.staffs_has_customers_list)
    # print(creator.staffs_has_customers)
    create_staff_has_customer(creator.staffs_has_customers)
