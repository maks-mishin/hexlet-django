from urllib.parse import urljoin

import requests

BASE_URL = 'http://localhost:5000'


def test_has_form():
    response = requests.get(urljoin(BASE_URL, '/users'))
    assert 'form' in response.text
    print('test_has_form passed')


def test_users():
    response = requests.get(urljoin(BASE_URL, '/users'))
    assert 'Warren' in response.text
    assert 'Amanda' in response.text
    print('test_users passed')


def test_starts_with_term():
    response = requests.get(urljoin(BASE_URL, '/users?term=al'))
    assert 'Alyssa' in response.text
    assert 'Alexa' in response.text
    assert 'Allison' in response.text
    assert 'Sarah' not in response.text
    print('test_starts_with_term passed')


def test_with_term_in_middle():
    response = requests.get(urljoin(BASE_URL, '/users?term=al'))
    assert 'Gerald' not in response.text
    assert 'Randall' not in response.text
    print('test_with_term_in_middle passed')


def test_not_found_term():
    response = requests.get(urljoin(BASE_URL, '/users?term=aaaaa'))
    assert 'aaaaa' in response.text
    print('test_not_found_term passed')


if __name__ == '__main__':
    test_has_form()
    test_users()
    test_with_term_in_middle()
    test_not_found_term()
    test_starts_with_term()
