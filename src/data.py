import random
import sys
import uuid

from faker import Faker
from flask import session

SEED = 1234


class Repository:
    def content(self):
        return session.values()

    def find(self, id):
        try:
            return session[id]
        except KeyError:
            sys.stderr.write(f'Wrong item id: {id}')
            raise

    def save(self, item):
        item['id'] = str(uuid.uuid4())
        session[item['id']] = item


def generate_companies(companies_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(companies_count))
    random.seed(SEED)
    random.shuffle(ids)

    companies = []
    for i in range(companies_count):
        companies.append({
            "id": ids[i],
            "name": fake.company(),
            "phone": fake.phone_number(),
        })
    return companies


def generate_users(users_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(1, users_count))
    random.seed(SEED)
    random.shuffle(ids)

    users = []
    for i in range(users_count - 1):
        users.append({
            'id': ids[i],
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.free_email(),
        })

    return users
