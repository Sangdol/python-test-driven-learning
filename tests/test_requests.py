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
    assert type(response.json()) == dict


def test_requests_data_vs_json():
    """
    data: application/x-www-form-urlencoded
    json: application/json
    """
    url = 'https://httpbin.org/post'

    data_response = requests.post(url, data={'a': 1})

    assert data_response.status_code == 200
    assert data_response.json()['data'] == ''
    assert data_response.json()['json'] is None
    assert data_response.json()['form'] == {'a': '1'}

    json_response = requests.post(url, json={'a': 1})

    assert json_response.json()['data'] == '{"a": 1}'
    assert json_response.json()['json'] == {'a': 1}
    assert json_response.json()['form'] == {}
