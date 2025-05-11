from faker import Faker
import random
from src.models import Transaction
from datetime import datetime, timedelta

faker = Faker()


def generate_fake_transactions(account_id: int, count: int = 20000):
    transactions = []
    for _ in range(count):
        amount = round(random.uniform(-1000, 1000), 2)
        description = faker.sentence(nb_words=5)
        timestamp = faker.date_time_between(start_date="-1y", end_date="now")

        tx = Transaction(
            account_id=account_id,
            amount=amount,
            description=description,
            timestamp=timestamp,
        )
        transactions.append(tx)
    return transactions
