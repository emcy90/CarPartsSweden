from controllers.cps_orders_controller import create_cps_orders


def main():
    cps_orders = {
        'order_date': '',
        'required_date': '',
        'shipping_date': '',
        'status': '',
        'comments': '',
        'order_no_comments': '',

    }

    create_cps_orders(cps_orders)


if __name__ == '__main__':
    main()
