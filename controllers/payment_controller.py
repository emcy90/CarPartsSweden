from data.repository import payment_repository


def get_payment_by_no(_id):
    return payment_repository.get_payment_by_no(_id)


def create_payment(payment):
    payment_repository.create_payment(payment)
