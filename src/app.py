import os

from flask import Flask, render_template, request, redirect, \
    url_for, flash, get_flashed_messages

from data import Repository
from validator import validate_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY',
    default='asidfuaybwhra28h3dq2dh'
)

users_repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/users/')
def users_get():
    users = users_repo.content()
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'users/index.html',
        users=users,
        messages=messages
    )


@app.post('/users/')
def users_post():
    user = request.form.to_dict()
    errors = validate_user(user)
    if errors:
        return render_template(
            'users/new.html',
            user=user,
            errors=errors
        ), 422
    users_repo.save(user)
    flash('User is created', 'success')
    return redirect(url_for('users_get'), code=302)


@app.route('/users/new/')
def users_new():
    user_placeholder = {
        'title': '',
        'paid': '',
        'email': ''
    }
    errors = {}
    return render_template(
        'users/new.html',
        course=user_placeholder,
        errors=errors
    )


@app.get('/users/<int:id>')
def users_page(id: int):
    user = users_repo.find(id)
    return render_template(
        'users/show.html',
        user=user
    )

