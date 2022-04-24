"""
Home        https://docs.python-requests.org/en/latest/
Quickstart  https://docs.python-requests.org/en/latest/user/quickstart/
"""
import requests


def test_requests():
    url = 'https://httpbin.org/get'
    params = {'param1': 'value1', 'param2': 'value2'}
    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.url == 'https://httpbin.org/get?param1=value1&param2=value2'
    assert response.json()['args'] == params
    assert response.json()['headers']['Host'] == 'httpbin.org'


def test_requests_with_headers():
    url = 'https://httpbin.org/get'

    # For some reason, the server capitalize the first character of header names
    # so the test will fail if the header name is not capitalized.
    headers = {'Param1': 'value1', 'Param2': 'value2'}
    response = requests.get(url, headers=headers)

    # print(response.json())
    assert response.status_code == 200
    assert response.url == 'https://httpbin.org/get'
    assert response.json()['headers'].items() >= headers.items()
    assert response.json()['headers']['Host'] == 'httpbin.org'

