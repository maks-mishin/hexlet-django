import random

from faker import Faker

SEED = 1234


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


def generate_posts(size):
    fake = Faker()
    fake.seed_instance(SEED)

    posts = []
    for _ in range(size):
        posts.append({
            'id': fake.uuid4(),
            'title': fake.sentence(),
            'body': fake.text(),
            'slug': fake.slug(),
        })
    return posts
