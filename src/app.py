import os

from flask import Flask, render_template, request, redirect, \
    url_for, flash, get_flashed_messages, make_response

from repository import PostsRepository, Repository
from validator import validate_user, validate_school, validate_post

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY',
    default='asidfuaybwhra28h3dq2dh'
)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/schools')
def school_list():
    schools_repo = Repository()
    schools = schools_repo.content()
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'schools/index.html',
        schools=schools,
        messages=messages
    )


@app.get('/schools/<id>')
def get_school_by_id(id):
    repo = Repository()
    school = repo.find(id)
    if not school:
        return 'Page not found', 404

    return render_template(
        'schools/show.html',
        school=school,
    )


@app.post('/schools')
def school_create():
    repo = Repository()
    data = request.form.to_dict()
    errors = validate_school(data)
    if errors:
        return render_template(
            'schools/new.html',
            school=data,
            errors=errors
        ), 422
    repo.save(data)
    flash('School has been created!', 'success')
    return redirect(url_for('school_list'))


@app.route('/schools/<id>/edit')
def school_edit(id):
    repo = Repository()
    school = repo.find(id)
    errors = []

    return render_template(
        'schools/edit.html',
        school=school,
        errors=errors
    )


@app.post('/schools/<id>/patch')
def school_patch(id):
    repo = Repository()
    school = repo.find(id)
    data = request.form.to_dict()
    errors = validate_school(data)

    if errors:
        return render_template(
            'schools/edit.html',
            school=school,
            errors=errors
        ), 422

    school['name'] = data['name']
    repo.save(school)
    flash('School has been updated', 'success')
    return redirect(url_for('school_list'))


@app.get('/users/')
def user_list():
    repo = Repository()
    users = repo.content()
    messages = get_flashed_messages(with_categories=True)
    return render_template(
        'users/index.html',
        users=users,
        messages=messages
    )


@app.post('/users/')
def user_create():
    repo = Repository()
    user = request.form.to_dict()
    errors = validate_user(user)
    if errors:
        return render_template(
            'users/new.html',
            user=user,
            errors=errors
        ), 422
    repo.save(user)
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
    repo = Repository()
    user = repo.find(id)
    return render_template(
        'users/show.html',
        user=user
    )


@app.route('/users/<id>/edit')
def user_edit(id):
    repo = Repository()
    user = repo.find(id)
    errors = []

    return render_template(
        'users/edit.html',
        user=user,
        errors=errors
    )


@app.post('/users/<id>/patch')
def user_patch(id):
    repo = Repository()
    user = repo.find(id)
    data = request.form.to_dict()
    errors = validate_user(data)

    if errors:
        return render_template(
            'users/edit.html',
            user=user,
            errors=errors
        ), 422

    user['first_name'] = data['first_name']
    user['last_name'] = data['last_name']
    user['email'] = data['email']
    repo.save(user)
    flash('User has been updated', 'success')
    return redirect(url_for('user_list'))


@app.route('/posts')
def post_list():
    repo = PostsRepository()
    # page_posts = 5
    posts = list(repo.content())
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
    repo = PostsRepository()
    post = repo.find(id)
    if not post:
        return 'Page not found', 404
    return render_template(
        'posts/show.html',
        post=post
    )


@app.post('/posts')
def post_create():
    repo = PostsRepository()
    post = request.form.to_dict()
    errors = validate_post(post)
    if errors:
        return render_template(
            'posts/new.html',
            post=post,
            errors=errors
        ), 422
    id = repo.save(post)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('post_list')))
    resp.headers['X-ID'] = id
    return resp


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


@app.get('/posts/<id>/update')
def post_edit(id):
    repo = PostsRepository()
    post = repo.find(id)
    errors = []

    return render_template(
        'posts/edit.html',
        post=post,
        errors=errors
    )


@app.post('/posts/<id>/update')
def post_update(id):
    repo = PostsRepository()
    post = repo.find(id)
    data = request.form.to_dict()
    errors = validate_post(data)

    if errors:
        return render_template(
            'posts/edit.html',
            post=post,
            errors=errors
        ), 422

    post['title'] = data['title']
    post['body'] = data['body']
    id = repo.save(post)
    flash('Post has been updated', 'success')
    resp = make_response(redirect(url_for('post_list')))
    resp.headers['X-ID'] = id
    return resp


@app.get('/courses')
def course_list():
    return 'Here will list of courses'
