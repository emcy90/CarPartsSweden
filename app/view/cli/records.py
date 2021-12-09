from app.view.cli.records_repository import get_records_by_name, get_records_by_order_no


def show_all():
    print("Input name: ")
    name = input()
    records = get_records_by_name(name)
    print("***********")
    print("All Records")
    print("***********")
    print()
    for record in records:
        print(record)


# def add_record():
#    pass


# def delete_record():
#    pass

def show_order():
    print("Input order no: ")
    order = input()
    records = get_records_by_order_no(order)
    print("***********")
    print("All Records")
    print("***********")
    for record in records:
        print(record)


if __name__ == '__main__':
    show_all()
