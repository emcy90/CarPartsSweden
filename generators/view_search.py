from data.models import Storage
from data.repository.view_search_repository import search_view_by_id, search_product_view_by_id
from generators import storage


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
    kalle = search_view_by_id(25)
    pelle = search_product_view_by_id(98)
    id_storage = 'storage_id'
    storage_name = 'storage_name'  # 'storage_name'
    storage_city = 'storage_city'
    storage_quantity = 'storage_quantity'
    product_id = 'product_id'
    a = (getattr(kalle, id_storage))
    b = (getattr(kalle, storage_name))
    c = (getattr(kalle, storage_city))
    d = (getattr(kalle, storage_quantity))
    e = (getattr(pelle, product_id))
    print(f'Id_storage:', {a}, 'storage_name', {b}, 'storage city', {c}, 'storage quantity', {d}, 'product id', {e})


if __name__ == '__main__':
    main()
