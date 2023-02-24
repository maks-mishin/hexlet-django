import os

from flask import Flask, render_template, request, redirect, \
    url_for, flash, get_flashed_messages

from repository import PostsRepository, Repository
from validator import validate_user, validate_school, validate_post

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY',
    default='asidfuaybwhra28h3dq2dh'
)
app.debug = True

posts_repo = Repository()
users_repo = Repository()
schools_repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/schools')
def school_list():
    schools = schools_repo.content()
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'schools/index.html',
        schools=schools,
        messages=messages
    )


@app.get('/schools/<id>')
def get_school_by_id(id):
    school = schools_repo.find(id)
    if not school:
        return 'Page not found', 404

    return render_template(
        'schools/show.html',
        school=school,
    )


@app.post('/schools')
def school_create():
    data = request.form.to_dict()
    errors = validate_school(data)
    if errors:
        return render_template(
            'schools/new.html',
            school=data,
            errors=errors
        ), 422
    schools_repo.save(data)
    flash('School has been created!', 'success')
    return redirect(url_for('school_list'))


@app.get('/users/')
def user_list():
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
    return redirect(url_for('user_list'), code=302)


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


@app.get('/users/<id>')
def user_detail(id):
    user = users_repo.find(id)
    return render_template(
        'users/show.html',
        user=user
    )


@app.route('/posts')
def post_list():
    # page_posts = 5
    posts = list(posts_repo.content())
    page = request.args.get('page', default=1, type=int)
    messages = get_flashed_messages(with_categories=True)

    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages,
        # posts=posts[
        #       (page - 1) * page_posts:page * page_posts
        #       ],
        page=page,
    )


@app.get('/posts/<id>')
def post_detail(id):
    post = posts_repo.find(id)
    if not post:
        return 'Page not found', 404
    return render_template(
        'posts/show.html',
        post=post
    )


@app.post('/posts')
def post_create():
    post = request.form.to_dict()
    errors = validate_post(post)
    if errors:
        return render_template(
            'posts/new.html',
            post=post,
            errors=errors
        ), 422
    posts_repo.save(post)
    flash('Post has been created', 'success')
    return redirect(url_for('post_list'), code=302)


@app.get('/posts/new')
def post_new():
    post_placeholder = {
        'title': '',
        'body': ''
    }
    errors = {}
    return render_template(
        'posts/new.html',
        post=post_placeholder,
        errors=errors
    )


@app.get('/courses')
def course_list():
    return 'Here will list of courses'
