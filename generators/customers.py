# from controllers.customer_controller import create_customer
from controllers.customer_controller import create_customer


def main():
    customer = {
        'first_name': 'Sune',
        'last_name': 'Karlsson',
        'company_name': '',
        'phone': '+46744246409',
        'adress1': 'Vintergatan 1',
        'adress2': '',
        'city': 'Göteborg',
        'zip_code': '44943',
        'country': 'Sweden',
        'sales_representant': 'Olle Berg',
        'states': ''

    }

    create_customer(customer)


if __name__ == '__main__':
    main()
