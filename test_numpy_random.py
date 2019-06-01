import numpy as np


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


# rand between a and b
# p(x) = 1 / (b - a)
def test_random_uniform():
    assert np.all(np.random.uniform(0, 1, 100) >= 0)
    assert np.all(np.random.uniform(0, 1, 100) < 1)


# https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do
def test_random_seed():
    np.random.seed(0)
    assert np.allclose(
        np.random.rand(4),
        [0.5488135, 0.71518937, 0.60276338, 0.54488318])

    # seed() applies only once
    assert not np.allclose(
        np.random.rand(4),
        [0.5488135, 0.71518937, 0.60276338, 0.54488318])


# standard normal distribution
def test_randn():
    assert_array_equal(np.random.randn(2, 3, 4).shape, (2, 3, 4))
