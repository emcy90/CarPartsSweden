from generators.cps_object import CpsCreator

# CREATING THE CREATOR OBJECT THAT HOLDS ALL INFO WE NEED TO CREATE OUR FAKE DATA.
creator = CpsCreator()
creator.load_all_data()

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

# CREATING A PAYMENT OBJECT
creator.assemble_payment_object()
creator.payment_list = [creator.payment_date, creator.payment_amount, creator.customer_paid_bill_id]
creator.create_payment_dict(creator.payment_key_list, creator.payment_list)
print(creator.payment)

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

# CREATING PRODUCTLINES OBJECT
# This needs a productline.txt file, text_description.txt and html_description.txt
# and image.txt to work, haven't got those files yet.
creator.assemble_productline_object()
creator.productline_list = [creator.productline, creator.text_description, creator.html_description,
                            creator.image]
creator.create_productline_dict(creator.productline_key_list, creator.productline_list)
print(creator.productline)

# CREATING PRODUCTS OBJECT


# CREATING ORDERDETAILS OBJECT


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
