from data.db import session
from data.models import Payment


def get_payment_by_no(_id):
    return session.query(Payment).filter(Payment.payments_no == _id).first()


def create_payment(payment):
    payment = Payment(**payment)
    session.add(payment)
    session.commit()
    print()
    print('Added payment successfully!')
