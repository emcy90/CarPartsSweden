# from controllers.customer_controller import create_customer
from controllers.customer_controller import create_customer


def main():
    customer = {
        'first_name': 'Kalle',
        'last_name': 'Andersson',
        'company_name': '',
        'phone': '+46731246409',
        'adress1': 'Dragsspelsgatan 10A',
        'adress2': '',
        'city': 'Göteborg',
        'zip_code': '44873',
        'country': 'Sweden',
        'sales_representant': 'Gösta Gustavsson',
        'states': '',
        # 'orders_order_no': '123'
    }

    create_customer(customer)


if __name__ == '__main__':
    main()
