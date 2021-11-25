from data.repository import customer_car_repository


def get_customer_cars_by_reg_no(_id):
    return customer_car_repository.get_customer_cars_by_reg_no(_id)


def create_car(car):
    customer_car_repository.create_car(car)
