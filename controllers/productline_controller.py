from data.repository import productline_repository


def get_productline_by_id(_id):
    return productline_repository.get_productline_by_id(_id)


def create_productline(productline):
    productline_repository.create_productline(productline)
    