from typing import Annotated, NamedTuple, get_type_hints


# No way to get a full name
# https://stackoverflow.com/questions/15165101/how-to-get-full-type-name-in-python
def test_module_and_name():
    assert type({}).__module__ == 'builtins'
    assert type({}).__name__ == 'dict'


# https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
def test_type_checking():
    assert type([]) is list
    assert type({}) is dict

    # isinstance is working for type inheritance
    assert isinstance({}, dict)


# https://docs.python.org/3/library/typing.html#typing.get_type_hints
def test_get_type_hints():
    class Student(NamedTuple):
        name: Annotated[str, 'some marker']

    assert get_type_hints(Student) == {'name': str}
    assert get_type_hints(Student, include_extras=False) == {'name': str}
    assert get_type_hints(Student, include_extras=True) == {'name': Annotated[str, 'some marker']}
