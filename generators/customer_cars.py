# from dll.repository.customer_car_repository import create_car
from app.bll import create_car


def main():
    car = {
        'reg_no': 'ABC 123',
        'manufacturer': 'Volvo cars',
        'color': 'rainbow',
        'model': 'V70',
        'year_model': '2011',
        'owner_id': '1'
    }

    create_car(car)


if __name__ == '__main__':
    main()
