"""
https://scikit-learn.org/stable/modules/learning_curve.html
"""
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
from sklearn.datasets import load_iris

np.random.seed(0)
iris = load_iris()
X, y = iris.data, iris.target
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]

train_size, train_scores, valid_scores, = learning_curve(
    SVC(kernel='linear'), X, y, train_sizes=[50, 80, 110], cv=5)

plt.figure()
plt.plot(train_size, train_scores.mean(axis=1), label='Train score')
plt.plot(train_size, valid_scores.mean(axis=1), label='Valid score')
plt.legend(loc=3)
plt.show()
