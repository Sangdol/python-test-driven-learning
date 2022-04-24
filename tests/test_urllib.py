from urllib.parse import urlparse, quote


def test_urlparse():
    o = urlparse('https://zalando.de/path/to/something?hello=world#fragment')

    assert o.scheme == 'https'
    assert o.netloc == 'zalando.de'
    assert o.path == '/path/to/something'
    assert o.query == 'hello=world'
    assert o.fragment == 'fragment'


def test_quote():
    """Similar to encodeURIComponent in JS.
    https://docs.python.org/3/library/urllib.parse.html#url-quoting
    """
    # safe='/' by default
    assert quote('/') == '/'
    assert quote('/', safe='') == '%2F'
    assert quote('#') == '%23'
    assert quote(':') == '%3A'
