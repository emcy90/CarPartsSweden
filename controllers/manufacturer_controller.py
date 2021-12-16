from data.repository import manufacturer_repository


def get_manufacturer_by_id(_id):
    return manufacturer_repository.get_manufacturer_by_id(_id)


def create_manufacture(manufacture):
    manufacturer_repository.create_manufacture(manufacture)
