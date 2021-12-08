from data.repository import records_repository


def get_records_by_name(name):
    return records_repository.get_records_by_name(name)


def get_records_by_order_no():
    return records_repository.get_records_by_order_no()


def get_records_by_staff_has_customer():
    return records_repository.get_records_by_staff_has_customer()


def get_all_records():
    return records_repository.get_all_records()


def show_records():
    pass
