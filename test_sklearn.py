import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.datasets import load_iris


def assert_array_equal(arr1, arr2):
    if not np.array_equal(arr1, arr2):
        raise ValueError("{} is not {}".format(arr1, arr2))


def test_roc_auc():
    # roc_acu_score can be used only for binary
    y_true = np.array([0, 0, 1, 1])
    y_scores = np.array([0.1, 0.4, 0.35, 0.8])
    assert metrics.roc_auc_score(y_true, y_scores) == 0.75

    # with this you can set 'pos_label'
    y = np.array([1, 1, 2, 2])
    pred = np.array([0.1, 0.4, 0.35, 0.8])
    fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
    assert metrics.auc(fpr, tpr) == 0.75


def test_grid_search_cv():
    iris = load_iris()

    svc = svm.SVC()
    clf = GridSearchCV(estimator=svc, param_grid={'kernel': ('linear', 'rbf'), 'C': [0.1, 10]}, cv=3)
    clf.fit(iris.data, iris.target)

    assert_array_equal(list(clf.cv_results_.keys()),
                       ['mean_fit_time', 'std_fit_time', 'mean_score_time',
                        'std_score_time', 'param_C', 'param_kernel', 'params',
                        'split0_test_score', 'split1_test_score', 'split2_test_score',
                        'mean_test_score', 'std_test_score', 'rank_test_score',
                        'split0_train_score', 'split1_train_score', 'split2_train_score',
                        'mean_train_score', 'std_train_score'])


def test_dummy_classifier():
    X = np.array([1, 2, 3]).reshape(-1, 1)
    y = [1, 1, 0]
    dummy_majority = DummyClassifier(strategy='most_frequent').fit(X, y)

    assert_array_equal(dummy_majority.predict(X), [1, 1, 1])

    dummy_stratified = DummyClassifier(strategy='stratified').fit(X, y)
    pred = dummy_stratified.predict(np.arange(100).reshape(-1, 1))
    no_of_1 = np.count_nonzero(pred)
    no_of_0 = len(pred) - no_of_1
    assert no_of_1 > no_of_0  # cannot guarantee but most possibly this would be true


def test_classification_report():
    y = [1, 1, 0, 0]
    y_pred = [1, 1, 1, 0]

    report = classification_report(y, y_pred)
    assert report == \
'''              precision    recall  f1-score   support

           0       1.00      0.50      0.67         2
           1       0.67      1.00      0.80         2

   micro avg       0.75      0.75      0.75         4
   macro avg       0.83      0.75      0.73         4
weighted avg       0.83      0.75      0.73         4
'''


def test_evaluation_metrics():
    y = [1, 1, 0, 0]
    y_pred = [1, 1, 1, 0]

    assert accuracy_score(y, y_pred) == 0.75
    assert precision_score(y, y_pred) == 2/3
    assert recall_score(y, y_pred) == 1
    assert f1_score(y, y_pred) == 0.8


def test_confusion_matrix():
    """
    Confusion matrix
    [[TN, FP],
    [FN, TP]]
    """
    y = [1, 1, 0, 0]
    y_pred = [0, 0, 1, 1]
    assert_array_equal(confusion_matrix(y, y_pred), [[0, 2], [2, 0]])

    y_pred = [1, 1, 1, 0]
    assert_array_equal(confusion_matrix(y, y_pred), [[1, 1], [0, 2]])


# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
def test_r2_score():
    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]

    assert np.isclose(r2_score(y_true, y_pred), 0.9486)

    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]

    assert r2_score(y_true, y_pred) == 1

    y_true = [1, 2, 3]
    y_pred = [2, 2, 2]

    assert r2_score(y_true, y_pred) == 0

    y_true = [1, 2, 3]
    y_pred = [3, 2, 1]

    assert r2_score(y_true, y_pred) == -3

    y_true = [1, 2, 3]
    y_pred = [6, 4, 1]

    assert r2_score(y_true, y_pred) == -15.5


def test_pipeline_linear_regression():
    model = Pipeline([('poly', PolynomialFeatures(degree=3)),
                      ('linear', LinearRegression())])

    X = np.array([1, 2, 3])
    y = [2, 4, 6]

    model.fit(X.reshape(-1, 1), y)
    pred = model.predict([[1]])

    assert np.isclose(pred[0], 2)


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
