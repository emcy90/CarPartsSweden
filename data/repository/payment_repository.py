from data.db import session
from data.models import Payment


def get_payment_by_no():
    payment_id = session.query(Payment.payments_no).all()
    payment_id_clean_list = []
    for _id in payment_id:
        payment_id_clean_list.append(_id[0])
    return payment_id_clean_list


def create_payment(payment):
    payment = Payment(**payment)
    session.add(payment)
    session.commit()
    print()
    print('Added payment successfully!')
    print()
    print('Added payment successfully!')
