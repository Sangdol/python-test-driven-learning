import unittest


class PythonBasicTest(unittest.TestCase):

    # https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
    def test_number_to_comma_str(self):
        self.assertEqual("{:,}".format(1000000.1234), '1,000,000.1234')
        self.assertEqual("{:,}".format(1000000), '1,000,000')

    # https://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
    def test_type_checking(self):
        self.assertTrue(type([]) is list)
        self.assertTrue(type({}) is dict)

        # isinstance is working for type inheritance
        self.assertTrue(isinstance({}, dict))

    # noinspection PyUnreachableCode
    # https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
    def test_raise_exception(self):
        try:
            raise ValueError('hello', 'world', '!')
            self.fail()
        except ValueError as err:
            self.assertEqual(err.args, ('hello', 'world', '!'))

    # https://stackoverflow.com/questions/8683178/chained-method-calls-indentation-style-in-python
    def test_newline(self):
        self.assertEqual(
            1000, 1000
        )

        self \
            .assertEqual(1000, 1000)

        (self
            .assertEqual(1000, 1000))

    # stars, asterisks
    # https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
    def test_extra_args(self):
        def test1(first, *args, **kwargs):
            return first, args, kwargs

        first, args, kwargs = test1(1, 2, 3, a=1, b="b")
        self.assertEqual(first, 1)
        self.assertEqual(args, (2, 3))
        self.assertEqual(kwargs, {"a": 1, "b": "b"})

        first, args, kwargs = test1(1, *(2, 3), **{"a": 1, "b": "b"})
        self.assertEqual(first, 1)
        self.assertEqual(args, (2, 3))
        self.assertEqual(kwargs, {"a": 1, "b": "b"})

    def test_if_statement(self):
        a = 10
        if a > 5:
            self.assertEqual('foo'.upper(), 'FOO')
        elif a == 11:
            self.fail()
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()
