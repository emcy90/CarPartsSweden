from controllers.storage_controller import create_storage


def main():
    storage = {
        'storage_name': '',
        'storage_quantity': '',
        'storage_city': ''

    }

    create_storage(storage)


if __name__ == '__main__':
    main()
