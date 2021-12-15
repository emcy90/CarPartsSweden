from bson.objectid import ObjectId
import random
from pymongo import MongoClient

from app.bll.customer_controller import view_single_mongo_customer, view_all_mongo_customers, insert_one_customer, \
    delete_one_mongo_customer

client = MongoClient(f"mongodb://root:slash@localhost:27017")
db = client.real_cps
my_col = db["test"]


def mongo_db_menu():
    print("*" * 50)
    print("Welcome to MongoDB")
    print("*" * 50)
    print("(1) customers collection")
    print()
    valet = str(input("> "))
    if valet == "1":
        print("========== Customer ==========")
        print()
        print("(1) View Customer")
        print("(2) View All Customers")
        print("(3) Add Customer")
        print("(4) Delete Customer")
        print("(5) Update Customer")
        print("(6) Go Back Main")
        valet2 = str(input("> "))
        if valet2 == "1":
            # ObjectId("61b70f8e568fb5974e0df0fe")
            xxx = str(input("Enter mongo object id (ex: 61b70f8e568fb5974e0df0fe):\n> "))
            view_single_mongo_customer(xxx)
            print()

        elif valet2 == "2":
            view_all_mongo_customers()

        elif valet2 == "3":
            insert_one_customer()

        elif valet2 == "4":
            xxx = str(input("Enter Mongo id object to delete a customer:\n> "))
            delete_one_mongo_customer(xxx)

        elif valet2 == "5":
            xxx = str(input("Enter Mongo id object to update a customer:\n> "))
            update_mongo_customer(xxx)
        elif valet2 == "6":
            pass



