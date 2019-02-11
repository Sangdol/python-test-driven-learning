import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


def test_pipeline_linear_regression():
    model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                      ('linear', LinearRegression())])

    X = np.array([1, 2, 3])
    y = [2, 4, 6]

    model.fit(X.reshape(-1, 1), y)
    assert model.predict([[1]]) == [2]


def test_min_max_scaler():
    X = list(zip(np.arange(0, 10), np.arange(1000, 1010)))

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    assert np.allclose(X_scaled[0], [0, 0])
    assert np.allclose(X_scaled[1], [0.1111111, 0.1111111])
    assert np.allclose(X_scaled[2], [0.2222222, 0.2222222])
    assert np.allclose(X_scaled[9], [1, 1])


# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
def test_train_test_split():
    X = y = np.arange(100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    assert len(X_train) == 75
    assert len(y_train) == 75
    assert len(X_test) == 25
    assert len(y_test) == 25

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

    assert len(X_train) == 50
    assert len(y_train) == 50
    assert len(X_test) == 50
    assert len(y_test) == 50


# https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset
def test_datasets_to_dataframe():
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris.data, iris.target],
                      columns=(iris.feature_names + ['target']))

    assert df.shape == (150, 5)


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
    assert_array_equal(np.unique(iris.target), [0, 1, 2])

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
