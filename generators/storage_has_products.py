from controllers.storage_has_products_controller import create_storage_has_product


def main():
    storage_has_product = {
        'storage_-storage_id': '',
        'products_product_id': ''
    }

    create_storage_has_product(storage_has_product)


if __name__ == '__main__':
    main()
