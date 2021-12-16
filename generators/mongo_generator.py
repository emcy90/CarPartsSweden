import pymongo
import random
from pymongo import MongoClient

# I think this import is needed if you want the feature of searching on
# mongo ids.
from bson.objectid import ObjectId

from app.bll.cps_orders_controller import mongo_create_cps_orders
from app.bll.customer_controller import mongo_create_customer
from app.bll.manufacturer_controller import mongo_create_manufacturer
from app.bll.order_controller import mongo_create_order
from app.bll.product_controller import mongo_create_product
from app.bll.staff_controller import mongo_create_staff
from app.bll.storage_controller import mongo_create_storage
from app.bll.supplier_controller import mongo_create_supplier
from generators.cps_object import CpsCreator

# client = MongoClient(f"mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
client = MongoClient(f"mongodb://root:slash@localhost:27017")
db = client.real_cps
my_col = db["test"]


# Here are som examples of how to add stuff to mongo db, and how to find stuff.
# all those things should go to repos later.

def add_one_item():
    clean_dict = {"Name": "Anna"}
    db.test.insert_one(clean_dict)
    print(f"added {clean_dict} to database: ")


def create_mongo_customer(customer):
    my_clean_dict = customer
    customer = Customer(**customer)
    print()
    db.customers.insert_one(my_clean_dict)
    print("Added mongo customer")


def create_super_customer_mongo(super_mongo_customer):
    super_mongo_customer_clean_dict = super_mongo_customer
    db.customers.insert_one(super_mongo_customer_clean_dict)
    print("Added Super Mongo customer successfully")


# Here are a ready made function to find all id, in mongo database
def find_all_mongo_id():
    get_all_mongo_id = []
    id_finder = db.customers.find()
    for id_items in id_finder:
        print(id_items['_id'])
        get_all_mongo_id.append(id_items['_id'])
    return get_all_mongo_id


# Here is the way you can search after a specific mongo ID
def find_one_specific_mongo_id():
    # id_finder = db.test.find()
    id_finder2 = db.test.find({"_id": ObjectId("61b70f8e568fb5974e0df0fe")})
    print(id_finder2)
    for mongo_customer in id_finder2:
        obj_id = (mongo_customer['_id'])
        namn = (mongo_customer['Name'])  # ['_id'])
        print(f'you did find: ObjectId {obj_id} and the name is: {namn} ')


# Here is an example function how to update data in mongo.
def update_mongo_customer():
    my_query = {"Name": "Anna"}
    new_values = {"$set": {"Name": "Anna2"}}

    db.test.update_one(my_query, new_values)

    # print "customers" after the update:
    for x in my_col.find():
        print(x)


def delete_mongo_customer():
    my_query = {"Name": "Mr.Slash"}
    my_col.delete_one(my_query)
    print(f"Deleted: {my_query} ")


def delete_a_collection():
    # Warning this will delete all stuff under a collection.
    x = my_col.delete_many({})
    print(x.deleted_count, " documents deleted.")


# Here are the working functions to do stuff, that we can add into the console app later.
# ***************************************************************************************

# add_one_item()
find_one_specific_mongo_id()


# find_all_mongo_id()
# update_mongo_customer()
# delete_mongo_customer()
# delete_a_collection()

# ****************************************************************************************
# Building a random function for mongo ids

def random_owner_ids_from_mongo_list(mongo_id_list):
    get_me_owner_id = random.choice(mongo_id_list)
    return get_me_owner_id


def random_customers_id_customers_from_mongo_list(mongo_id_list):
    get_me_customers_id_customers = random.choice(mongo_id_list)
    return get_me_customers_id_customers


def random_customers_paid_bill_id_from_mongo_list(mongo_id_list):
    get_me_customer_paid_bill_id = random.choice(mongo_id_list)
    return get_me_customer_paid_bill_id


def random_staffs_id_staff_from_mongo_list(staffs_id_list):
    get_me_staffs_id_staff = random.choice(staffs_id_list)
    return get_me_staffs_id_staff


def random_orders_no_from_counter_list():
    counter = load_order_no()
    get_me_orders_no = random.randint(1, counter)
    return get_me_orders_no


# Making an object from the class


mongo_creator = CpsCreator()
mongo_creator.load_all_data()
mongo_id_list = find_all_mongo_id()
staffs_id_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
counter = 1
counter_cps_orders = 1
counter_manufacturer_id = 1
counter_supplier_id = 1
payments_counter_no = 1

print(mongo_id_list)


def save_order_no():
    with open('C:/skolan/CarPartsSweden/MongoDB/counter.txt', 'w', encoding="utf-8") as f:
        f.write((str(counter)))


def load_order_no():
    f = open('mongo/counter.txt', 'r')
    co = f.readlines()
    num = 0
    num = int(co[-1])
    f.close()
    return num


def save_counter_supplier_id():
    with open('mongo/counter_supplier.txt', 'w', encoding="utf-8") as f:
        f.write((str(counter)))


def load_counter_supplier_id():
    f = open('mongo/counter_supplier.txt', 'r')
    co = f.readlines()
    num = 0
    num = int(co[-1])
    f.close()
    return num


def save_counter_cps_orders_id():
    with open('mongo/counter_cps_orders.txt', 'w', encoding="utf-8") as f:
        f.write((str(counter)))


def load_counter_cps_orders_id():
    f = open('mongo/counter_cps_orders.txt', 'r')
    co = f.readlines()
    num = 0
    num = int(co[-1])
    f.close()
    return num


def save_counter_manufacturer_id():
    with open('mongo/counter_manufacturer.txt', 'w', encoding="utf-8") as f:
        f.write((str(counter)))


def load_counter_manufacturer_id():
    f = open('mongo/counter_manufacturer.txt', 'r')
    co = f.readlines()
    num = 0
    num = int(co[-1])
    f.close()
    return num


def save_counter_payments_no():
    with open('mongo/counter_payments_no.txt', 'w', encoding="utf-8") as f:
        f.write((str(counter)))


def load_counter_payments_no():
    f = open('mongo/counter_payments_no.txt', 'r')
    co = f.readlines()
    num = 0
    num = int(co[-1])
    f.close()
    return num


# Creating 10 clean customers to MONGO DB
# for i in range(0, 20):
#     mongo_creator.assemble_customer_object()
#     mongo_creator.customer_list = [mongo_creator.first_name, mongo_creator.last_name, mongo_creator.company,
#                                    mongo_creator.phone,
#                                    mongo_creator.street_adress + " " + mongo_creator.house_number, '',
#                                    mongo_creator.city, mongo_creator.zip_code,
#                                    mongo_creator.country, mongo_creator.my_sales_representant, mongo_creator.state]
#     mongo_creator.create_customer_dict(mongo_creator.customer_key_list, mongo_creator.customer_list)
#     # mg = creator.create_customer_dict(creator.customer_key_list, creator.customer_list)
#     # print(creator.customer)
#     mongo_create_customer(mongo_creator.customer)

# Loading all the counters
counter_order_no = load_order_no()
counter_supplier_id = load_counter_supplier_id()
counter_cps_orders_id = load_counter_cps_orders_id()
counter_manufacturer_id = load_counter_manufacturer_id()
counter_payments_no = load_counter_payments_no()

our_sales_staff_list = ['Barbro Lindgren', 'Maja Glad', 'Anneli Lund', 'Bobbo Nyqvist', 'Jonas Karlsson',
                        'Mimmi Johnsson',
                        'Lisa Svensson']

# CREATING CUSTOMERS COLLECTION

for i in range(0, 20):
    mongo_id_list = find_all_mongo_id()
    owner_id = random_owner_ids_from_mongo_list(mongo_id_list)
    customer_id = random_customers_id_customers_from_mongo_list(mongo_id_list)
    customer_paid_bill_id = random_customers_paid_bill_id_from_mongo_list(mongo_id_list)
    # ?staffs_id_staff = random_staffs_id_staff_from_mongo_list(staffs_id_list)
    staffs_id_staff = random.choice(our_sales_staff_list)

    mongo_creator.assemble_customer_object()
    mongo_creator.assemble_car_object(mongo_creator.all_cars_ids)
    mongo_creator.assemble_payment_object()
    mongo_creator.customer_list = [mongo_creator.first_name, mongo_creator.last_name, mongo_creator.company,
                                   mongo_creator.phone,
                                   mongo_creator.street_adress + " " + mongo_creator.house_number, '',
                                   mongo_creator.city, mongo_creator.zip_code,
                                   mongo_creator.country, mongo_creator.my_sales_representant, mongo_creator.state,
                                   mongo_creator.reg_no, mongo_creator.manufacturer, mongo_creator.color,
                                   mongo_creator.model,
                                   mongo_creator.year_model, owner_id, counter_payments_no, mongo_creator.payment_date,
                                   mongo_creator.payment_amount, customer_paid_bill_id,
                                   staffs_id_staff, customer_id]
    mongo_creator.create_super_customer_mongo_dict(mongo_creator.super_customer_key_list_mongo,
                                                   mongo_creator.customer_list)
    mongo_create_customer(mongo_creator.super_mongo_customer_collection)
    owner_id = None
    customer_paid_bill_id = None
    customer_id = None

    # CREATING ORDERS COLLECTION
    customer_id = random_customers_id_customers_from_mongo_list(mongo_id_list)
    mongo_creator.assemble_order_object()
    mongo_creator.assemble_orderdetails_object()
    xx_order_no = random_orders_no_from_counter_list()
    mongo_creator.order_list = [counter_order_no, mongo_creator.order_date, mongo_creator.required_date,
                                mongo_creator.shipping_date,
                                mongo_creator.status, mongo_creator.comments,
                                customer_id, xx_order_no,
                                mongo_creator.products_product_id, mongo_creator.quantity,
                                mongo_creator.price_each]
    mongo_creator.create_super_order_mongo_dict(mongo_creator.super_order_key_list_mongo,
                                                mongo_creator.order_list)
    mongo_create_order(mongo_creator.super_mongo_order_collection)
    customer_id = None

    # Here goes product and product description
    # we have to make a random product id, from our product list.
    product_id_list = mongo_creator.all_product_ids
    product_id = random.choice(product_id_list)
    product_name = random.choice(mongo_creator.product_name)
    product_description = random.choice(mongo_creator.product_description)
    inprice = mongo_creator.random_inprice()
    outprice = mongo_creator.random_outprice()
    product_description = random.choice(mongo_creator.product_description)
    text_description = random.choice(mongo_creator.text_description)
    html_description = random.choice(mongo_creator.html_description)
    mongo_creator.product_list = [product_id, product_name, product_description,
                                  inprice,
                                  outprice, product_description,
                                  text_description, html_description,
                                  mongo_creator.image, product_id]
    mongo_creator.create_super_product_mongo_dict(mongo_creator.super_product_key_list_mongo,
                                                  mongo_creator.product_list)
    mongo_create_product(mongo_creator.super_mongo_product_collection)

    # CREATING SUPPLIERS COLLECTION (slumpa supplier och suppliers_suppliers_id)
    mongo_creator.assemble_supplier_object()
    mongo_creator.assemble_suppliers_has_cps_orders_object()
    suppliers_supplier_id = random.randint(1, counter_supplier_id)
    cps_orders_internal_order_no = random.randint(1, counter_cps_orders_id)
    mongo_creator_supplier_list = [counter_supplier_id, mongo_creator.supplier_name, mongo_creator.supplier_adress1,
                                   mongo_creator.supplier_adress2, mongo_creator.city, mongo_creator.zip_code,
                                   mongo_creator.country, mongo_creator.suppliers_contact_person,
                                   mongo_creator.phone_number,
                                   mongo_creator.email, suppliers_supplier_id,
                                   cps_orders_internal_order_no]
    mongo_creator.create_super_supplier_mongo_dict(mongo_creator.super_supplier_key_list_mongo,
                                                   mongo_creator_supplier_list)
    mongo_create_supplier(mongo_creator.super_mongo_supplier_collection)

    # CREATING MANUFACTURERS COLLECTION
    # create a counter for manufacturer id, because its auto increment
    # manufacturers_manufacturer_id shall be random
    # cps_orders_internal should be random
    mongo_creator.assemble_manufacturers_object()
    mongo_creator.assemble_manufacturers_has_cps_orders_object()
    manufacturers_manufacturer_id = random.randint(1, counter_manufacturer_id)
    cps_orders_internal_order_no = random.randint(1, counter_cps_orders_id)
    mongo_creator_manufacturer_list = [counter_manufacturer_id, mongo_creator.name_manufacturer,
                                       mongo_creator.main_office_adress1,
                                       mongo_creator.main_office_adress2, mongo_creator.main_office_name,
                                       mongo_creator.manufacturer_contact_person,
                                       mongo_creator.contact_person_phone,
                                       mongo_creator.contact_person_email, manufacturers_manufacturer_id,
                                       cps_orders_internal_order_no]
    mongo_creator.create_super_munufacturer_mongo_dict(mongo_creator.super_munufacturer_key_list_mongo,
                                                       mongo_creator_manufacturer_list)
    mongo_create_manufacturer(mongo_creator.super_mongo_manufacturer_collection)

    # CREATING CPS ORDERS COLLECTION
    # make internal_order_no as a counter , because its an auto increment field.
    # staffs_id_staff should be random, cps_order_internal should be random
    mongo_creator.assemble_cps_orders_object()
    mongo_creator.assemble_staffs_has_cps_orders_object()
    our_sales_staff_list = ['Barbro Lindgren', 'Maja Glad', 'Anneli Lund', 'Bobbo Nyqvist', 'Jonas Karlsson',
                            'Mimmi Johnsson',
                            'Lisa Svensson']

    staffs_id_staff = random.choice(our_sales_staff_list)
    cps_orders_internal_order_no = random.randint(1, counter_cps_orders_id)
    internal_order_no = counter_cps_orders_id

    mongo_creator_cps_orders_list = [internal_order_no, mongo_creator.order_date, mongo_creator.required_date,
                                     mongo_creator.shipping_date,
                                     mongo_creator.status, mongo_creator.comments, mongo_creator.order_no_comments,
                                     staffs_id_staff, cps_orders_internal_order_no]
    mongo_creator.create_super_cps_orders_mongo_dict(mongo_creator.super_cps_orders_key_list_mongo,
                                                     mongo_creator_cps_orders_list)
    mongo_create_cps_orders(mongo_creator.super_mongo_cps_orders_collection)

    # CREATING STAFF COLLECTION
    # id_staff should be a counter , reports_to should be random from id_staff counter.
    our_boss_list = ['Gunnar Grinig', 'Lova Urbansson', 'Petra Malmgren', 'Per Olsson', 'Amanda Lilja',
                     'Jessica Berg']
    reports_to = random.choice(our_boss_list)
    mongo_creator.assemble_staffs_object()
    id_staff = random.choice(our_sales_staff_list)
    first_name, last_name = id_staff.split(" ")
    mongo_creator_staff_list = [id_staff, first_name, last_name, mongo_creator.job_title,
                                mongo_creator.phone, mongo_creator.store, reports_to]
    mongo_creator.create_super_staff_mongo_dict(mongo_creator.super_staff_key_list_mongo,
                                                mongo_creator_staff_list)
    mongo_create_staff(mongo_creator.super_mongo_staff_collection)

    # CREATING STORAGE COLLECTION
    mongo_creator.assemble_storage_object()
    mongo_creator.assemble_storage_has_products_object()
    short_storage_id_list = [1, 2, 3]
    selected_storage_id = random.randint(1, len(short_storage_id_list))
    if selected_storage_id == 1:
        mongo_creator.storage_city = "Göteborg"
        storage_id = selected_storage_id
        mongo_creator.storage_name = "Nyponet"
    elif selected_storage_id == 2:
        mongo_creator.storage_city = "Malmö"
        storage_id = selected_storage_id
        mongo_creator.storage_name = "Rosen"
    elif selected_storage_id == 3:
        mongo_creator.storage_city = "Stockholm"
        storage_id = selected_storage_id
        mongo_creator.storage_name = "Kvisten"

    storage_storage_id = random.choice(short_storage_id_list)
    product_id_list = mongo_creator.all_product_ids
    products_product_id = random.choice(product_id_list)

    mongo_creator_storage_list = [storage_id, mongo_creator.storage_name, mongo_creator.storage_quantity,
                                  mongo_creator.storage_city, storage_storage_id,
                                  products_product_id]
    mongo_creator.create_super_storage_mongo_dict(mongo_creator.super_storage_key_list_mongo,
                                                  mongo_creator_storage_list)
    mongo_create_storage(mongo_creator.super_mongo_storage_collection)

    # Increment the counters for each round
    counter_order_no += 1
    counter_supplier_id += 1
    counter_cps_orders_id += 1
    counter_payments_no += 1

    # Save the counters for each round
    save_order_no()
    save_counter_supplier_id()
    save_counter_cps_orders_id()
    save_counter_payments_no()
