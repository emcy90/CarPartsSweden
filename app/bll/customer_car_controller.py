from app.dll.repository import customer_car_repository


def get_customer_cars_by_reg_no():
    return customer_car_repository.get_customer_cars_by_reg_no()


def create_car(car):
    customer_car_repository.create_car(car)
