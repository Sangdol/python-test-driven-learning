import unittest


class ListComprehensionTest(unittest.TestCase):

    def test_list_comprehension(self):
        self.assertEqual(list(map(lambda x: x ** 2, range(3))), [0, 1, 4])
        self.assertEqual([x ** 2 for x in range(3)], [0, 1, 4])

        comb = [(x, y) for x in [1, 2] for y in [2, 3] if x != y]
        self.assertEqual(comb, [(1, 2), (1, 3), (2, 3)])


if __name__ == '__main__':
    unittest.main()
