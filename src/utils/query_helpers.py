from src.models import Customer


def get_first_five_customers(db_session):
    return db_session.query(Customer).limit(5).all()


