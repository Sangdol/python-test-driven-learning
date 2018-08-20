import unittest

class SyntaxTest(unittest.TestCase):

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
