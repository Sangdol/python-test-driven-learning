import unittest
import numpy as np

class NumpyTest(unittest.TestCase):

    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equal.html
    def assertArrayEqual(self, arr1, arr2):
        self.assertTrue(np.array_equal(arr1, arr2))

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
