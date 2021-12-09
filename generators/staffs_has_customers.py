from app.bll import create_staff_has_customer


def main():
    staff_has_customer = {
        'staffs_id_staff': '',
        'customers_id_customers': ''
    }

    create_staff_has_customer(staff_has_customer)


if __name__ == '__main__':
    main()
