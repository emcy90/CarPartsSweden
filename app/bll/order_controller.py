from app.dll.repository import order_repository
from pymongo import MongoClient

client = MongoClient('mongodb://root:slash@localhost:27017')
db = client.real_cps


def get_order_by_no():
    return order_repository.get_order_by_id()


def create_order(order):
    order_repository.create_order(order)


def mongo_create_order(super_order):
    return order_repository.mongo_create_order(super_order)


def show_order(order):
    return order_repository.show_order(order)
