import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
def test_linear_regression():
    X = pd.DataFrame({'a': [1, 1, 2, 2], 'b': [1, 2, 2, 3]})
    y = np.array([6, 8, 9, 11])  # dot 1 2 + 3

    reg = LinearRegression().fit(X, y)

    assert np.isclose(reg.score(X, y), 1)
    assert np.allclose(reg.coef_, np.array([1., 2.]))
    assert np.isclose(reg.intercept_, 3)

    assert np.allclose(reg.predict(np.array([[1, 1]])), np.array([6]))
    assert np.allclose(reg.predict(pd.DataFrame({'a': [1], 'b': [2]})), np.array([8]))
    assert np.allclose(reg.predict(pd.DataFrame({'a': [2], 'b': [1]})), np.array([7]))

    # it doesn't care about column names
    assert np.allclose(reg.predict(pd.DataFrame({'b': [1], 'a': [2]})), np.array([8]))
