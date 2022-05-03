import pytest

from collections import OrderedDict, defaultdict, Counter


def test_basic():
    x = {"hello": "world"}
    assert x["hello"] == "world"

    if "hello" not in x:
        pytest.fail()

    x["hallo"] = "welt"
    assert x["hallo"] == "welt"

    keys = ""
    for key in x:
        keys += key

    assert keys == "hellohallo"

    values = ""
    for value in x.values():
        values += value

    assert values == "worldwelt"

    key_value = ""
    for key, value in x.items():
        key_value += key + value

    assert key_value == "helloworldhallowelt"


def test_list_to_dictionary():
    l = [("a", 1), ("b", 2)]

    assert dict(l) == {"a": 1, "b": 2}


# https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
def test_dictionary_view_objects():
    x = {"a": 1, "b": 2}

    assert list(x) == ["a", "b"]
    assert list(x.keys()) == ["a", "b"]
    assert list(x.values()) == [1, 2]
    assert list(x.items()) == [("a", 1), ("b", 2)]


def test_dictionary_functions():
    x = {"hello": "world"}

    assert x.get("hi", "default") == "default"


def test_sort_keys():
    d = {"a": 3, "b": 2, "c": 1}

    assert sorted(d) == ["a", "b", "c"]
    assert sorted(d, key=lambda x: d[x]) == ["c", "b", "a"]
    assert sorted(d, key=lambda x: d[x], reverse=True) == ["a", "b", "c"]


def test_sort_dict():
    d = {"a": 3, "b": 2, "c": 1}

    dict(sorted(d.items())) == {"a": 3, "b": 2, "c": 1}
    dict(sorted(d.items(), key=lambda item: item[1])) == {"a": 3, "b": 2, "c": 1}


#
# https://docs.python.org/3/library/collections.html#collections.defaultdict
#
def test_defaultdict():
    d = defaultdict(list)
    d["a"].append(1)
    assert d["a"] == [1]

    d["a"].append(2)
    assert d["a"] == [1, 2]


def test_defaultdict_dict():
    d = defaultdict(dict)
    d["a"]["b"] = 1
    assert d["a"] == {"b": 1}


def test_defaultdict_assigning_other_type():
    d = defaultdict(list)

    # This works but type error occurs.
    d["a"] = 1  # type: ignore
    assert d["a"] == 1


def test_nested_defaultdict():
    d = defaultdict(lambda: defaultdict(list))

    d["a"]["b"].append(1)
    assert d["a"]["b"] == [1]

    d["a"]["b"].append(2)
    assert d["a"]["b"] == [1, 2]


#
# https://docs.python.org/3/library/collections.html#collections.OrderedDict
#
# The insert-order is preserved in dict from Python 3.7
# so OrderedDict is less needed but there's some additional features
# https://stackoverflow.com/questions/50872498/will-ordereddict-become-redundant-in-python-3-7
def test_ordered_dict():
    # LIFO / Stack

    d = OrderedDict.fromkeys("abc")
    assert list(d.items()) == [("a", None), ("b", None), ("c", None)]

    d.move_to_end("b")
    assert list(d.items()) == [("a", None), ("c", None), ("b", None)]

    e = d.popitem()
    assert e == ("b", None)

    d["d"] = None
    assert list(d.items()) == [("a", None), ("c", None), ("d", None)]

    e = d.popitem()
    assert e == ("d", None)

    # FIFO / Queue

    e = d.popitem(last=False)
    assert e == ("a", None)


#
# A Counter is a dict subclass for counting hashable objects.
# https://docs.python.org/3/library/collections.html#collections.Counter
#
def test_counter():
    c = Counter(["a", "a", "b"])

    assert c["a"] == 2
    assert c["c"] == 0
    assert list(c.elements()) == ["a", "a", "b"]
    assert c.most_common() == [("a", 2), ("b", 1)]
    assert c.most_common(1) == [("a", 2)]

    c2 = Counter("ab")

    assert c2["a"] == 1
    assert c2["c"] == 0

    c3 = Counter("aaabbc")
    c3.subtract(Counter("aabbcc"))

    assert c3["a"] == 1
    assert c3["b"] == 0
    assert c3["c"] == -1
    assert list(c3.elements()) == ["a"]

    c3.update("aa")
    assert c3["a"] == 3
    assert list(c3.elements()) == ["a", "a", "a"]


def test_contains_other_dict():
    """
    https://stackoverflow.com/questions/9323749/how-to-check-if-one-dictionary-is-a-subset-of-another-larger-dictionary
    """
    d1 = {"a": 1, "b": 2}
    d2 = {"a": 1, "b": 2, "c": 3}

    assert d1.items() <= d2.items()
    assert all(item in d2.items() for item in d1.items())


def test_merging_dicts():
    """
    https://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression
    """
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}

    d3 = {**d1, **d2}
    assert d3 == {"a": 1, "b": 2, "c": 3, "d": 4}

    d4 = {**d1, **d2, "e": 5}
    assert d4 == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

    d_to_update = {"a": 1, "b": 2}
    d_to_update.update(d2)
    assert d_to_update == {"a": 1, "b": 2, "c": 3, "d": 4}
