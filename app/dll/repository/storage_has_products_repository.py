from app.dll.db import session
from app.dll.models import StorageHasProducts

from app.dll.repository.view_search_repository import search_view_by_id, search_product_view_by_id


# def main():
#    our_storage_id = int(input('Enter the storage id: '))
#    our_product_id = int(input('Enter the product id: '))

#    kalle = our_view_storage_and_product_view(our_storage_id, our_product_id)
#    print(kalle)


def our_view_storage_and_product_view(our_storage_id, our_product_id):
    storages = search_view_by_id(our_storage_id)
    produkten = search_product_view_by_id(our_product_id)
    data = (f'Storage id: {storages.storage_id}, Storage Name: {storages.storage_name}'
            f', Storage Quantity: {storages.storage_quantity}, Storage City: {storages.storage_city},'
            f' Product id: {produkten.product_id}, Product description: {produkten.product_description}')

    return data


def get_storage_has_products_by_id():
    storage_product = session.query(StorageHasProducts.storage_storage_id).all()
    storage_has_products_id_clean_list = []
    for _id in storage_product:
        storage_has_products_id_clean_list.append(_id[0])
    return storage_has_products_id_clean_list


def get_storage_products_product_by_id():
    products_product = session.query(StorageHasProducts.products_product_id).all()
    products_product_by_id_clean_list = []
    for _id in products_product:
        products_product_by_id_clean_list.append(_id[0])
    return products_product_by_id_clean_list


def create_storage_has_product(storage_has_product):
    storage_has_product = StorageHasProducts(**storage_has_product)
    session.add(storage_has_product)
    session.commit()
    print()
    print('Added storage has product successfully!')
