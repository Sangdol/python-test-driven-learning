"""
https://scikit-learn.org/stable/modules/learning_curve.html
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
iris = load_iris()
X, y = iris.data, iris.target
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]

alpha = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(Ridge(), X, y, 'alpha',
                                              alpha, cv=5)


plt.figure()
plt.semilogx(alpha, train_scores.mean(axis=1), label='Train score')
plt.semilogx(alpha, valid_scores.mean(axis=1), label='Valid score')
plt.legend(loc=3)
plt.show()
