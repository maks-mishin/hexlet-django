from flask import Flask, jsonify, request, render_template

from data import generate_companies, generate_users

companies = generate_companies(100)
users = generate_users(100)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/companies')
def get_companies():
    page = request.args.get('page', 1, type=int)
    per = request.args.get('per', 5, type=int)
    return jsonify(companies[(page - 1) * per:page * per])


@app.route('/users/<int:id>')
def get_user_by_id(id: int):
    user_list = list(filter(lambda user: user['id'] == id, users))
    if not user_list:
        return 'Page not found', 404
    return render_template('users/show.html', user=user_list[0])


@app.route('/users')
def get_all_users():
    return render_template('users/index.html', users=users)


@app.route('/companies/<int:id>')
def get_company_by_id(id: int):
    company = list(filter(lambda c: c['id'] == id, companies))
    if company:
        return jsonify(company[0])
    return 'Page not found', 404


@app.route('/courses/<id>')
def courses(id: int):
    return f'Course id: {id}'
