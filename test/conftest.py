import pytest
from src.db import init_db
from src.models import Account
from test.factories import generate_fake_transactions


@pytest.fixture(scope="function")
def db_session():
    session = init_db()
    yield session
    session.close()


@pytest.fixture
def populated_account(db_session):
    account = Account(owner_name="Test User", balance=0.0)
    db_session.add(account)
    db_session.commit()

    transactions = generate_fake_transactions(account.id, count=500)
    db_session.add_all(transactions)
    db_session.commit()

    return account
