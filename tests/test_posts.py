from urllib.parse import urljoin

import requests

BASE_URL = 'http://localhost:8080'


# def test_fisrt_page():
#     response = requests.get(urljoin(BASE_URL, '/posts'))
#     assert 'Theory key since close film available' in response.text
#     assert 'Approach onto clearly newspaper' in response.text
#
#
# def test_second_page():
#     response = requests.get(urljoin(BASE_URL, '/posts?page=2'))
#     prev_page = '?page=1'
#     next_page = '?page=3'
#     assert prev_page in response.text
#     assert next_page in response.text
#
#     assert 'Theory key since close film available' not in response.text
#     assert 'Economic at stay staff store no' in response.text
#
#
# def test_get_post():
#     response = requests.get(urljoin(BASE_URL, '/posts/always-discuss-move'))
#     assert 'Approach onto clearly newspaper' in response.text
#     assert 'Visit side whatever.' in response.text
#
#
# def test_post_not_found():
#     response = requests.get(urljoin(BASE_URL, '/posts/not-found-post'))
#     assert response.status_code == 404
#     assert 'Page not found' in response.text

def test_form():
    response = requests.get(urljoin(BASE_URL, '/posts/new'))
    assert 'title' in response.text
    assert 'body' in response.text


def test_wrong_post_data():
    data = {'title': '', 'body': ''}
    response = requests.post(urljoin(BASE_URL, '/posts'), data=data)
    assert response.status_code == 422
    assert "Can&#39;t be blank" in response.text

    data = {'title': 'Foobar', 'body': ''}
    response = requests.post(urljoin(BASE_URL, '/posts'), data=data)
    assert response.status_code == 422
    assert "Can&#39;t be blank" in response.text
    assert 'Foobar' in response.text

    data = {'title': '', 'body': 'Barbaz'}
    response = requests.post(urljoin(BASE_URL, '/posts'), data=data)
    assert response.status_code == 422
    assert "Can&#39;t be blank" in response.text
    assert 'Barbaz' in response.text


def test_create_posts():
    with requests.Session() as s:
        data = {'title': 'first', 'body': 'first_body'}
        response = s.post(urljoin(BASE_URL, '/posts'), data=data)

        assert 'Post has been created' in response.text
        assert 'first' in response.text

        data = {'title': 'second', 'body': 'second_body'}
        response = s.post(urljoin(BASE_URL, '/posts'), data=data)

        assert 'Post has been created' in response.text
        assert 'first' in response.text
        assert 'second' in response.text