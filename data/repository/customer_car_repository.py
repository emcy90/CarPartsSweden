from data.db import session
from data.models import CustomerCar


def get_customer_cars_by_reg_no():
    # return session.query(CustomerCar.reg_no).all()
    # return session.query(CustomerCar).filter(CustomerCar.reg_no == _id).first()

    reg_no = session.query(CustomerCar.reg_no).all()
    car_reg_no_clean_list = []
    for no in reg_no:
        car_reg_no_clean_list.append(no[0])
    return car_reg_no_clean_list

    # WITH COMPREHENSION
    # reg_no = session.query(Customer.id_customers).all()
    # car_reg_no_clean_list = [no[0] for no in reg_no]
    # return car_reg_no_clean_list

def create_car(car):
    car = CustomerCar(**car)
    session.add(car)
    session.commit()
    print()
    print('Added customer car successfully!')
