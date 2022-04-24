"""
https://github.com/getsentry/responses
"""
import responses
import requests
import re


@responses.activate
def test_responses():
    url = 'https://test.com'
    responses.add(
        responses.POST,
        url,
        json={'a': 1}, status=200)

    assert requests.post(url).content == b'{"a": 1}'


@responses.activate
def test_multiple_responses():
    url = 'https://test.com'
    responses.add(
        responses.POST,
        url,
        json={'a': 1}, status=200)
    responses.add(
        responses.POST,
        url,
        json={'a': 1}, status=200)
    responses.add(
        responses.POST,
        url,
        json={'a': 2}, status=200)

    assert requests.post(url).content == b'{"a": 1}'
    assert requests.post(url).content == b'{"a": 1}'
    assert requests.post(url).content == b'{"a": 2}'
    assert requests.post(url).content == b'{"a": 2}'


@responses.activate
def test_responses_url_pattern():
    url = re.compile('https://test.com/')
    responses.add(
        responses.POST,
        url,
        json={'a': 1}, status=200)

    assert requests.post(
        'https://test.com/abc?a=1&b=2',
        headers={'Content-Type': 'application/json; charset=UTF-8'},
    ).content == b'{"a": 1}'

