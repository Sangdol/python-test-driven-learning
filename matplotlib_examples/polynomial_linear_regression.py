import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split


n = 15

x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)


def predictions():
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.pipeline import Pipeline

    degrees = [1, 3, 6, 9]
    res = []
    x = np.linspace(0, 10, 100).reshape(-1, 1)

    for degree in degrees:
        model = Pipeline([('poly', PolynomialFeatures(degree=degree)),
                          ('linear', LinearRegression())])
        model.fit(X_train.reshape(-1, 1), y_train)
        res.append(model.predict(x))

    return np.array(res)


def plot(degree_predictions):
    plt.figure(figsize=(10,5))
    plt.plot(X_train, y_train, 'o', label='training data', markersize=10)
    plt.plot(X_test, y_test, 'o', label='test data', markersize=10)
    for i,degree in enumerate([1,3,6,9]):
        plt.plot(np.linspace(0,10,100), degree_predictions[i], alpha=0.8, lw=2, label='degree={}'.format(degree))
    plt.ylim(-1,2.5)
    plt.legend(loc=4)
    plt.show()


plot(predictions())
