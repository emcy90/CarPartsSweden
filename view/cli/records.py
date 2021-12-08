from controllers.records_controllers import get_records_by_name, get_records_by_order_no, get_records_by_staff_has_customer


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

if __name__ == '__main__':
    show_all()




