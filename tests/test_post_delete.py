from urllib.parse import urljoin

import requests

BASE_URL = 'http://localhost:8080'


def test_template_has_post():
    with requests.Session() as s:
        data = {'title': 'title', 'body': 'body'}
        response = s.post(urljoin(BASE_URL, '/posts'), data=data, allow_redirects=False)
        response = s.get(urljoin(BASE_URL, '/posts'))
        assert ('method="post"' in response.text) or ("method='post'" in response.text)


def test_delete_post():
    with requests.Session() as s:
        data = {'title': 'first', 'body': 'first_body'}
        response = s.post(urljoin(BASE_URL, '/posts'), data=data, allow_redirects=False)
        id = response.headers['X-ID']
        assert response.status_code == 302

        data = {'title': 'second', 'body': 'second_body'}
        response = s.post(urljoin(BASE_URL, '/posts'), data=data, allow_redirects=False)
        id = response.headers['X-ID']
        response = s.post(urljoin(BASE_URL, f'/posts/{id}/delete'), allow_redirects=False)
        response = s.get(urljoin(BASE_URL, '/posts'))
        assert data['title'] not in response.text


def test_get_method_not_allowed():
    with requests.Session() as s:
        data = {'title': 'first', 'body': 'first_body'}
        response = s.post(urljoin(BASE_URL, '/posts'), data=data, allow_redirects=False)
        id = response.headers['X-ID']

        response = s.get(urljoin(BASE_URL, f'/posts/{id}/delete'), allow_redirects=False)
        assert response.status_code == 405  # GET method not allowed for delete forms
