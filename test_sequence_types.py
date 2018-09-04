import unittest


class SequenceTest(unittest.TestCase):

    def test_tuple(self):
        t = (1, 'a', 2, 'b')
        self.assertEqual(len(t), 4)

        # unpacking
        a, b = ('a', 'b')
        self.assertEqual(a, 'a')

    def test_list(self):
        l = [1, 2, 3]
        self.assertEqual(len(l), 3)

        l.append(4)
        self.assertEqual(len(l), 4)

        self.assertEqual([1] + [2], [1, 2])
        self.assertEqual([1] * 3, [1, 1, 1])
        self.assertTrue(1 in [1, 2])

        # slice
        self.assertEqual('hello'[0:2], 'he')
        self.assertEqual('hello'[-4:-2], 'el')
        self.assertEqual('hello'[-2:], 'lo')
        self.assertEqual('hello'[:3], 'hel')
        self.assertEqual('hello'[3:], 'lo')

        # string
        self.assertTrue('he' in 'hello')
        self.assertEqual('he' * 3, 'hehehe')
        self.assertEqual('hello world'.split(' ')[-1], 'world')

    def test_dictionary(self):
        x = {'hello': 'world'}
        self.assertEqual(x['hello'], 'world')

        x['hallo'] = 'welt'
        self.assertEqual(x['hallo'], 'welt')

        keys = ''
        for key in x:
            keys += key

        self.assertEqual(keys, 'hellohallo')

        values = ''
        for value in x.values():
            values += value

        self.assertEqual(values, 'worldwelt')

        key_value = ''
        for key, value in x.items():
            key_value += (key + value)

        self.assertEqual(key_value, 'helloworldhallowelt')


if __name__ == '__main__':
    unittest.main()
