from controllers.staffs_has_cps_orders_controller import create_staff_has_cps_order


def main():
    staff_has_cps_order = {
        'staff_id_staff': '',
        'cps_orders_internal_order_no': ''
    }

    create_staff_has_cps_order(staff_has_cps_order)


if __name__ == '__main__':
    main()
