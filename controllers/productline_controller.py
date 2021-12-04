from data.repository import productline_repository


def get_productline_by_id():
    return productline_repository.get_productline_by_id()


def create_productline(productline):
    productline_repository.create_productline(productline)
    