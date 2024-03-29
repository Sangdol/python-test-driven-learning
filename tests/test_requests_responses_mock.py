"""
https://github.com/getsentry/responses
"""
import functools
import responses
import requests
import re

from responses import matchers


# A way to set timeout globally: https://stackoverflow.com/a/59317604/524588
s = requests.Session()
s.request = functools.partial(s.request, timeout=0.1)


@responses.activate
def test_responses():
    url = 'https://test.com'
    responses.add(responses.POST, url, json={'a': 1}, status=200)

    assert s.post(url).content == b'{"a": 1}'


@responses.activate
def test_multiple_responses():
    url = 'https://test.com'
    responses.add(responses.POST, url, json={'a': 1}, status=200)
    responses.add(responses.POST, url, json={'a': 1}, status=200)
    responses.add(responses.POST, url, json={'a': 2}, status=200)

    assert s.post(url).content == b'{"a": 1}'
    assert s.post(url).content == b'{"a": 1}'
    assert s.post(url).content == b'{"a": 2}'
    assert s.post(url).content == b'{"a": 2}'


@responses.activate
def test_responses_url_pattern():
    url = re.compile('https://test.com/')
    responses.add(responses.POST, url, json={'a': 1}, status=200)

    assert (
        s.post(
            'https://test.com/abc?a=1&b=2',
            headers={'Content-Type': 'application/json; charset=UTF-8'},
        ).content
        == b'{"a": 1}'
    )


@responses.activate
def test_responses_matchers_header():
    url = 'https://test.com/'
    headers1 = {'header1': 'value1'}
    headers2 = {'header2': 'value2'}

    responses.add(
        responses.POST,
        url,
        match=[matchers.header_matcher(headers1)],
        json={'a': 1},
        status=200,
    )

    responses.add(
        responses.POST,
        url,
        match=[matchers.header_matcher(headers2)],
        json={'a': 2},
        status=200,
    )

    assert (
        s.post(
            'https://test.com/',
            headers=headers1,
        ).content
        == b'{"a": 1}'
    )

    assert (
        s.post(
            'https://test.com/',
            headers=headers2,
        ).content
        == b'{"a": 2}'
    )


@responses.activate
def test_responses_json_params_matcher():
    url = 'https://test.com/'

    responses.post(
        url=url,
        match=[matchers.json_params_matcher({"abc": 1})],
        status=200,
    )

    assert s.post(url, json={"abc": 1}).ok
    assert s.request("POST", url, json={"abc": 1}).ok


@responses.activate
def test_responses_call_count():
    url = 'https://test.com/'

    rsp = responses.get(url=url, status=200)

    assert s.get(url).ok
    assert rsp.call_count == 1
