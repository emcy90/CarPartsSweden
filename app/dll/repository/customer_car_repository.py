from app.dll.db import session
from app.dll.models import CustomerCar


def get_customer_cars_by_reg_no():
    reg_no = session.query(CustomerCar.reg_no).all()
    car_reg_no_clean_list = []
    for no in reg_no:
        car_reg_no_clean_list.append(no[0])
    return car_reg_no_clean_list


def create_car(car):
    car = CustomerCar(**car)
    session.add(car)
    session.commit()
    print()
    print('Added customer car successfully!')
