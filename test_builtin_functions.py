import unittest

class BuiltinFunctionsTest(unittest.TestCase):

    def test_map(self):
        names = ['sanghyun lee', 'hyunji kim']

        def lastname(name):
            return name.split(' ')[1]

        self.assertEqual(list(map(lastname, names)), ['lee', 'kim'])

if __name__ == '__main__':
    unittest.main()
