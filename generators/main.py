from controllers.customer_car_controller import create_car, get_customer_cars_by_reg_no
from controllers.customer_controller import create_customer
from controllers.order_controller import create_order
from controllers.orderdetails_controller import create_order_details
from controllers.payment_controller import create_payment
from controllers.product_controller import get_product_by_id
from controllers.productline_controller import create_productline
from data.repository.customer_repositroy import get_customer_by_id
from data.repository.order_repository import get_order_by_id

from generators.cps_object import CpsCreator

# CREATING THE CREATOR OBJECT THAT HOLDS ALL INFO WE NEED TO CREATE OUR FAKE DATA.
creator = CpsCreator()
creator.load_all_data()


# CALLING FUNCTIONS ----> CONTROLLER ----> REPOSITORY ----> DB
def calling_multicreate():
    # create_customer(creator.customer)
    # create_car(creator.customer_car)
    # create_payment(creator.payment)
    # create_order(creator.order)
    # create_productline(creator.productline)
    create_order_details(creator.orderdetails)


all_cars_ids = get_customer_cars_by_reg_no()
all_customers_ids = get_customer_by_id()
all_order_no = get_order_by_id()
all_product_ids = get_product_by_id()

print(f'All customers id: {all_customers_ids}')
print(f'All cars ids: {all_cars_ids}')
print(f'All order ids: {all_order_no}')
print(f'All product ids: {all_product_ids}')
print()

# CREATING A CUSTOMER OBJECT
creator.assemble_customer_object()
creator.customer_list = [creator.first_name, creator.last_name, creator.company, creator.phone,
                         creator.street_adress + " " + creator.house_number, '', creator.city, creator.zip_code,
                         creator.country, creator.my_sales_representant, creator.state]
creator.create_customer_dict(creator.customer_key_list, creator.customer_list)
print(creator.customer)

# CREATING A CAR OBJECT
creator.assemble_car_object()
customer_car_list = [creator.reg_no, creator.manufacturer, creator.color, creator.model,
                     creator.year_model, creator.owner_id]
creator.create_customer_car_dict(creator.customer_car_key_list, customer_car_list)
print(creator.customer_car)
# calling_multicreate()

# CREATING A PAYMENT OBJECT
creator.assemble_payment_object()
creator.payment_list = [creator.payment_date, creator.payment_amount, creator.customer_paid_bill_id]
creator.create_payment_dict(creator.payment_key_list, creator.payment_list)
print(creator.payment)
# calling_multicreate()

# GET RANDOM CUSTOMER.CUSTOMER_ID
creator.rnd_number_function()
# print(creator.rnd_number)

# Creating a order object  -----> How to have customer id less than numbers of customers when creating an order id
# CREATING ORDER OBJECT
creator.assemble_order_object()
creator.order_list = [creator.order_date, creator.required_date, creator.shipping_date,
                      creator.status, creator.comments, creator.customers_id_customers]
creator.create_order_dict(creator.order_key_list, creator.order_list)
print(creator.order)
# calling_multicreate()

# CREATING PRODUCTLINES OBJECT
# This needs a productline.txt file, text_description.txt and html_description.txt
# and image.txt to work, haven't got those files yet.
creator.assemble_productline_object()
creator.productline_list = [creator.productline, creator.text_description, creator.html_description,
                            creator.image]
creator.create_productline_dict(creator.productline_key_list, creator.productline_list)
print(creator.productline)
# calling_multicreate()

# CREATING PRODUCTS OBJECT
creator.assemble_products_object()
creator.products_list = [creator.product_name, creator.product_description, creator.inprice,
                         creator.outprice, creator.productlines]
creator.create_product_dict(creator.product_key_list, creator.products_list)
print(creator.product)

# CREATING ORDERDETAILS OBJECT
creator.assemble_orderdetails_object()
creator.orderdetails_list = [creator.orders_order_no, creator.products_product_id, creator.quantity,
                             creator.price_each]
creator.create_orderdetails_dict(creator.orderdetails_key_list, creator.orderdetails_list)
print(creator.orderdetails)
# calling_multicreate()

# CREATING STORAGE OBJECT


# CREATING STORAGE HAS PRODUCTS OBJECT


# CREATING SUPPLIERS OBJECT


# CREATING CPS ORDERS OBJECT


# CREATING SUPPLIERS HAS CPS ORDERS OBJECT


# CREATING MANUFACTURERS OBJECT


# CREATING MANUFACTURERS HAS CPS ORDERS OBJECT


# CREATING STAFFS OBJECT


# CREATING STAFFS HAS CPS ORDERS OBJECT


# CREATING STAFFS HAS STAFFS


# CREATING STAFFS HAS CUSTOMERS OBJECT
