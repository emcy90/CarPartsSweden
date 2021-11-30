# from controllers.customer_controller import create_customer
from controllers.customer_controller import create_customer


def main():
    customer = {
        'first_name': 'Anders',
        'last_name': 'Nilsson',
        'company_name': 'Din sko',
        'phone': '+46749898765',
        'adress1': 'Enebergsgatan 1',
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
