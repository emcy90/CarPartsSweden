from app.dll.repository.view_search_repository import search_view_by_id, search_product_view_by_id


# def __repr__(self):
#     return f"Storage(name='{self.storage.name}' quantity='{self.storage.storage_quantity}' storage city='{self.storage.storage_city}')".__repr__()
#
#
# def main():
#     kalle = search_view_by_id(25)
#
#     for i in kalle.__iter__()(): #__dict__(Storage):
#         a = i
#     print(kalle.__repr__())
#         #print(i, kalle[i])
#
#     # for items in kalle.__repr__(): #Kalle.__repr__():
#     #     item = kalle
#     # print(kalle.__repr__())

def main():
    our_storage_id = int(input('Enter the storage id: '))
    our_product_id = int(input('Enter the product id: '))

    kalle = our_view_storage_and_product_view(our_storage_id, our_product_id)
    print(kalle)
    # id_storage = 'storage_id'
    # storage_name = 'storage_name'  # 'storage_name'
    # storage_city = 'storage_city'
    # storage_quantity = 'storage_quantity'
    # product_id = 'product_id'
    # a = (getattr(kalle, id_storage))
    # b = (getattr(kalle, storage_name))
    # c = (getattr(kalle, storage_city))
    # d = (getattr(kalle, storage_quantity))
    # e = (getattr(pelle, product_id))
    # print(f'Id_storage:', {a}, 'storage_name', {b}, 'storage city', {c}, 'storage quantity', {d}, 'product id', {e})


def our_view_storage_and_product_view(our_storage_id, our_product_id):
    storages = search_view_by_id(our_storage_id)
    produkten = search_product_view_by_id(our_product_id)
    data = (f'Storage id: {storages.storage_id}, Storage Name: {storages.storage_name}'
            f', Storage Quantity: {storages.storage_quantity}, Storage City: {storages.storage_city},'
            f' Product id: {produkten.product_id}, Product description: {produkten.product_description}')

    return data


if __name__ == '__main__':
    main()
