from controllers.order_controller import create_order


def main():
    order = {
        'order_date': '2020-12-28',
        'required_date': '2020-12-31',
        'shipping_date': '2020-12-29',
        'status': 'NOK',
        'comments': 'Customer has not paid hes last bill.',
        'customers_id_customers': '1'

    }

    create_order(order)


if __name__ == '__main__':
    main()
