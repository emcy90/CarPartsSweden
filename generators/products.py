from controllers.product_controller import create_product


def main():
    product = {
        'product_name': 'Wheel',
        'product_description.txt': 'A black wheel',
        'inprice': '1000',
        'outprice': '2000',
        'productlines': 'Saab'

    }

    create_product(product)


if __name__ == '__main__':
    main()
