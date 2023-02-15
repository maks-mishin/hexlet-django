from urllib.parse import urljoin

import requests

BASE_URL = 'http://localhost:8080'


def test_companies():
    expected = [
            {
                'name': 'Wilson-Davis',
                'phone': '001-011-530-0059'
            },
            {
                'name': 'Gilbert-Hernandez',
                'phone': '(108)731-8719'
            },
            {
                'name': 'Davis, Riley and Adams',
                'phone': '+1-147-543-3780'
            },
            {
                'name': 'Jones, Cook and Mckinney',
                'phone': '+1-620-197-2183x20518'
            },
            {
                'name': 'Santiago Group',
                'phone': '6402424270'
            }
        ]

    response = requests.get(urljoin(BASE_URL, '/companies'))
    assert response.json() == expected


def test_companies_slice1():
    expected = [
        {'name': 'Davis, Riley and Adams', 'phone': '+1-147-543-3780'}
    ]
    response = requests.get(urljoin(BASE_URL, '/companies?page=3&per=1'))
    assert response.json() == expected


def test_companies_slice2():
    expected = [
        {'name': 'Thompson-Thompson', 'phone': '523-186-0248'},
        {'name': 'Reed Inc', 'phone': '800-670-4239x790'}
    ]
    response = requests.get(urljoin(BASE_URL, '/companies?page=20&per=2'))
    assert response.json() == expected
