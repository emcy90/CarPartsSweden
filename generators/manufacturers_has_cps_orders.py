from controllers.manufacturers_has_cps_orders_controller import create_manufacturer_has_cps_order


def main():
    manufacturer_has_cps_order = {
        'manufacturers_manufacturer_id': '',
        'cps_orders_internal_order_no': ''

    }

    create_manufacturer_has_cps_order(manufacturer_has_cps_order)


if __name__ == '__main__':
    main()
