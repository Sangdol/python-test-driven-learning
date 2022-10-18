"""
https://github.com/getsentry/responses
"""
import responses
import requests
import re

from responses import matchers


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


@responses.activate
def test_responses_matchers_header():
    url = 'https://test.com/'
    headers1 = {'header1': 'value1'}
    headers2 = {'header2': 'value2'}

    responses.add(
        responses.POST,
        url,
        match=[matchers.header_matcher(headers1)],
        json={'a': 1}, status=200)

    responses.add(
        responses.POST,
        url,
        match=[matchers.header_matcher(headers2)],
        json={'a': 2}, status=200)

    assert requests.post(
        'https://test.com/',
        headers=headers1,
    ).content == b'{"a": 1}'

    assert requests.post(
        'https://test.com/',
        headers=headers2,
    ).content == b'{"a": 2}'

