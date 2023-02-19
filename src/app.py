from flask import Flask, jsonify, request

from data import generate_companies

companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    return 'go to the /companies'


@app.get('/companies')
def get_companies():
    page = request.args.get('page', 1, type=int)
    per = request.args.get('per', 5, type=int)
    return jsonify(companies[(page - 1) * per:page * per])


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'