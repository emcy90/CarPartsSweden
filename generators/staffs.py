from controllers.staff_controller import create_staff


def main():
    staff = {
        'first_name': '',
        'last_name': '',
        'job_title': '',
        'phone': '',
        'reports_to': '',
        'store': ''

    }

    create_staff(staff)


if __name__ == '__main__':
    main()
