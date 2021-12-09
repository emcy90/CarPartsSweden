from app.bll.orderdetails_controller import create_order_details


def main():
    orderdetails = {
        'quantity': '20',
        'price_each': '1500',
        'orders_order_no': '2',
        'products_product_id': '3'
    }

    create_order_details(orderdetails)


if __name__ == '__main__':
    main()
