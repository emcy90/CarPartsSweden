from controllers.productline_controller import create_productline


def main():
    productline = {
        'productline': 'Saab',
        'text_description': 'A nice Saab',
        'html_description': '<h1>Saab</h1>',
        'image': 'Saab.jpg'

    }

    create_productline(productline)


if __name__ == '__main__':
    main()
