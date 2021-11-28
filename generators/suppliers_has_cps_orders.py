from controllers.suppliers_has_cps_orders_controller import create_suppliers_has_cps_order


def main():
    suppliers_has_cps_order = {
        'suppliers_supplier_id': '',
        'cps_orders_internal_order_no': ''

    }

    create_suppliers_has_cps_order(suppliers_has_cps_order)


if __name__ == '__main__':
    main()
