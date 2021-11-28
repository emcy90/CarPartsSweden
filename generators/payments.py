from controllers.payment_controller import create_payment


def main():
    payment = {
        'payment_date': '2018-01-30',
        'payment_amount': '120',
        'customer_paid_bill_id': '1'
    }

    create_payment(payment)


if __name__ == '__main__':
    main()
