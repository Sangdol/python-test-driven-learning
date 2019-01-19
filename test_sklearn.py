import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
def test_datasets():
    iris = load_iris()
    assert type(iris).__module__ == 'sklearn.utils'
    assert type(iris).__name__ == 'Bunch'

    assert_array_equal(list(iris), ['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])
    assert iris.data.shape == (150, 4)
    assert type(iris.data).__name__ == 'ndarray'
    assert iris.target.shape == (150,)
    assert type(iris.target).__name__ == 'ndarray'

    assert iris.filename.find('sklearn/datasets/data/iris.csv') > -1  # file location

    assert_array_equal(iris.feature_names,
                       ['sepal length (cm)', 'sepal width (cm)',
                        'petal length (cm)', 'petal width (cm)'])
    assert_array_equal(iris.target_names, ['setosa', 'versicolor', 'virginica'])

    data, target = load_iris(return_X_y=True)
    assert data.shape == (150, 4)
    assert target.shape == (150,)


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
