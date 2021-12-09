from app.dll.repository import payment_repository


def get_payment_by_no():
    return payment_repository.get_payment_by_no()


def create_payment(payment):
    payment_repository.create_payment(payment)
