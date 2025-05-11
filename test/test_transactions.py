from src.models import Account, Transaction
from sqlalchemy import text



def test_account_transaction(db_session):
    # Create an account
    account = Account(owner="Alice", balance=100.0)
    db_session.add(account)
    db_session.commit()

    # Add a transaction
    txn = Transaction(account_id=account.id, amount=-25.0)
    db_session.add(txn)
    db_session.commit()

    # Refresh account and validate
    db_session.refresh(account)
    total = sum(tx.amount for tx in account.transactions)
    assert total == -25.0
    assert len(account.transactions) == 1



def test_raw_sql_fetch_customers(db_session):
    result = db_session.execute(text("SELECT id, owner, balance FROM accounts LIMIT 5")).mappings()
    for row in result:
        print(dict(row))  # Now each `row` is a mapping (dict-like)



