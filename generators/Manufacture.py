from controllers.manufacturer_controller import create_manufacture


def main():

    manufacture = {
        'name_manufacturer': 'Volvo Penta',
        'main_office_address1': 'Fredrikasgård 9',
        'main_office_address2': '-',
        'main_office_name': 'Volvo Göteborg',
        'contact_person_name': 'Sven Svensson',
        'contact_person_phone': '+46764538904',
        'contact_person_email': 'sven.sven@gmail.com'

    }

    create_manufacture(manufacture)


if __name__ == '__main__':
    main()
