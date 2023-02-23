import os

from flask import Flask, render_template, request, redirect, \
    url_for, flash, get_flashed_messages

from data import Repository
from validator import validate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY',
    default='asidfuaybwhra28h3dq2dh'
)

repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index.html',
        courses=courses,
    )


@app.post('/courses')
def courses_post():
    course = request.form.to_dict()
    errors = validate(course)
    if errors:
        return render_template(
            'courses/new.html',
            course=course,
            errors=errors
        ), 422
    repo.save(course)
    return redirect(url_for('courses_get'), code=302)


@app.route('/courses/new')
def courses_new():
    course = {
        'title', '',
        'paid', ''
    }
    errors = {}
    return render_template(
        'courses/new.html',
        course=course,
        errors=errors
    )