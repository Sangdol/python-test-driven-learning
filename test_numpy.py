import unittest
import numpy as np
import pandas as pd
import collections


class NumpyTest(unittest.TestCase):

    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equal.html
    def assertArrayEqual(self, arr1, arr2):
        if not np.array_equal(arr1, arr2):
            self.fail("{} is not {}".format(arr1, arr2))

    # https://stackoverflow.com/questions/36000993/numpy-isnan-fails-on-an-array-of-floats-from-pandas-dataframe-apply
    def test_isnan_type_error(self):
        arr = np.array([np.nan, 0], dtype=object)
        try:
            """
            np.isnan can be applied to NumPy arrays of native dtype (such as np.float64):
            """
            np.isnan(arr)
            self.fail()
        except TypeError:
            self.assertArrayEqual(pd.isnull(arr), [True, False])
            pass

    def test_argwhere(self):
        arr = np.array([0, 0, np.nan, 1, 1, 1])
        
        self.assertArrayEqual(np.argwhere(arr == 0), [[0], [1]])
        self.assertArrayEqual(np.argwhere(np.isnan(arr)), [[2]])

    # https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray-in-python
    def test_counting(self):
        y = np.array([0, 0, 1, 1, 1])
        self.assertEqual(np.sum(y), 3)
        self.assertEqual(np.count_nonzero(y), 3)
        self.assertEqual(collections.Counter(y), {0: 2, 1: 3})
        self.assertEqual(len(y[y == 1]), 3)
        self.assertEqual((y == 1).sum(), 3)
        self.assertEqual(list(y).count(1), 3)

    # For conditional (ternary) operation
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html
    def test_where(self):
        x = np.array([1, 2, 3])
        self.assertArrayEqual(np.where(x >= 2, x, 0), [0, 2, 3])

    def test_transpose(self):
        self.assertArrayEqual(np.transpose([1, 2]), [1, 2])
        self.assertArrayEqual(np.transpose([[1, 2]]), [[1], [2]])

    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
    def test_arange(self):
        self.assertArrayEqual(np.arange(3), [0, 1, 2])

        # start, stop, step
        self.assertArrayEqual(np.arange(10, 16, 2), [10, 12, 14])

        # https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
        self.assertArrayEqual(np.arange(3, 5) == [3, 4], [True, True])
        self.assertTrue((np.arange(3, 5) == [3, 4]).all())


if __name__ == '__main__':
    unittest.main();
