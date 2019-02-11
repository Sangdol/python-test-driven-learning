from urllib.parse import urlparse


def test_urlparse():
    o = urlparse('https://zalando.de/path/to/something?hello=world#fragment')

    assert o.scheme == 'https'
    assert o.netloc == 'zalando.de'
    assert o.path == '/path/to/something'
    assert o.query == 'hello=world'
    assert o.fragment == 'fragment'
