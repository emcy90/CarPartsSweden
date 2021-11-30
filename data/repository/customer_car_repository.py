from data.db import session
from data.models import CustomerCar


def get_customer_cars_by_reg_no(_id):
    return session.query(CustomerCar).filter(CustomerCar.reg_no == _id).first()


def create_car(car):
    car = CustomerCar(**car)
    session.add(car)
    session.commit()
    print()
    print('Added customer car successfully!')
