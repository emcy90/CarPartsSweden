from app.dll.repository import manufacturer_repository


def get_manufacturer_by_id():
    return manufacturer_repository.get_manufacturer_by_id()


def create_manufacture(manufacture):
    manufacturer_repository.create_manufacture(manufacture)
