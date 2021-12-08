from controllers.supplier_controller import create_supplier


def main():
    supplier = {
        'supplier_name': '',
        'supplier_adress1': '',
        'supplier_adress2': '',
        'city': '',
        'zip_code': '',
        'country': '',
        'contact_person': '',
        'phone_number': '',
        'email': ''
    }

    create_supplier(supplier)


if __name__ == '__main__':
    main()
