# https://docs.python.org/3/library/unittest.html

import unittest


class UnitTestTest(unittest.TestCase):

    def test_assert(self):
        self.assertEqual('foo'.upper(), 'FOO')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    @unittest.skip("skip this")
    def test_nothing(self):
        self.fail("shouldn't happen")


if __name__ == '__main__':
    unittest.main()
