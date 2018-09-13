import unittest


class SyntaxTest(unittest.TestCase):

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
