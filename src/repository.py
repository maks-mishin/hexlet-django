import json
import sys
import uuid

from flask import session

from data import generate_posts, generate_users


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


class PostsRepository():
    def __init__(self):
        if 'posts' not in session:
            session['posts'] = {}

    def content(self):
        return session['posts'].values()

    def find(self, id):
        try:
            return session['posts'][id]
        except KeyError:
            sys.stderr.write(f'Wrong post id: {id}')
            raise

    def destroy(self, id):
        del session['posts'][id]

    def save(self, post):
        if not (post.get('title') and post.get('body')):
            raise Exception(f'Wrong data: {json.loads(post)}')
        if not post.get('id'):
            post['id'] = str(uuid.uuid4())
        session['posts'][post['id']] = post
        session['posts'] = session['posts']
        return post['id']


class SchoolsRepository():
    def __init__(self):
        if 'schools' not in session:
            session['schools'] = {}

    def content(self):
        return session['schools'].values()

    def find(self, id):
        try:
            return session['schools'][id]
        except KeyError:
            sys.stderr.write(f'Wrong school id: {id}')
            raise

    def destroy(self, id):
        del session['schools'][id]

    def save(self, school):
        if not (school.get('name')):
            raise Exception(f'Wrong data: {json.loads(school)}')
        if not school.get('id'):
            school['id'] = str(uuid.uuid4())
        session['schools'][school['id']] = school
        session['schools'] = session['schools']
        return school['id']


class UsersRepository():
    def __init__(self):
        if 'users' not in session:
            session['users'] = {}

    def content(self):
        return session['users'].values()

    def find(self, id):
        try:
            return session['users'][id]
        except KeyError:
            sys.stderr.write(f'Wrong user id: {id}')
            raise

    def destroy(self, id):
        del session['users'][id]

    def save(self, user):
        if not (user.get('first_name') and user.get('last_name') and user.get('email')):
            raise Exception(f'Wrong data: {json.loads(user)}')
        if not user.get('id'):
            user['id'] = str(uuid.uuid4())
        session['users'][user['id']] = user
        session['users'] = session['users']
        return user['id']