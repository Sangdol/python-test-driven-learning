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
