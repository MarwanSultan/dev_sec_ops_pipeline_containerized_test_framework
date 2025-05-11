import pytest
from sqlalchemy import func
from datetime import timedelta

from src.models import Customer, Transaction  # Adjust path as needed

def test_detect_suspicious_accounts(db_session):
    # 1. Accounts with more than 20 transactions in an hour
    bursty_accounts = db_session.query(
        Transaction.customer_id,
        func.count(Transaction.id).label("txn_count")
    ).group_by(Transaction.customer_id, func.strftime('%Y-%m-%d %H', Transaction.timestamp)) \
     .having(func.count(Transaction.id) > 20).all()

    # 2. Accounts with > $5,000 withdrawn in < 1 day
    draining_accounts = db_session.query(
        Transaction.customer_id,
        func.sum(Transaction.amount).label("withdrawal_total")
    ).filter(Transaction.amount < 0) \
     .group_by(Transaction.customer_id, func.date(Transaction.timestamp)) \
     .having(func.sum(Transaction.amount) < -5000).all()

    # 3. Accounts with negative balance
    negative_balance_accounts = db_session.query(
        Customer
    ).filter(Customer.balance < 0).all()

    assert not bursty_accounts, f"Bursty activity detected: {bursty_accounts}"
    assert not draining_accounts, f"Large withdrawal patterns detected: {draining_accounts}"
    assert not negative_balance_accounts, f"Negative balances found: {[c.id for c in negative_balance_accounts]}"
