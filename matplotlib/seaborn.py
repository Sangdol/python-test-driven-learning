import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

np.random.seed(1234)

v1 = pd.Series(np.random.normal(0, 10, 1000), name='v1')
v2 = pd.Series(2 * v1 + np.random.normal(60, 15, 1000), name='v2')
v3 = np.concatenate((v1, v2))

iris_raw = load_iris()
names = pd.Series(map(lambda i: iris_raw.target_names[i], iris_raw.target))
iris = pd.DataFrame(data=np.c_[iris_raw.data, names],
                    columns=(iris_raw.feature_names + ['Name']))


def two_hist():
    plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label='v1')
    plt.hist(v2, alpha=0.7, bins=np.arange(-50, 150, 5), label='v2')
    plt.legend()


def stacked_hist_and_kde():
    plt.hist([v1, v2], histtype='barstacked', normed=True)
    sns.kdeplot(v3)


def dist_plot():
    # we can pass keyword arguments for each individual component of the plot
    sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'})


def joint_plot():
    grid = sns.jointplot(v1, v2, alpha=0.4)
    grid.ax_joint.set_aspect('equal')


def hex_joint_plot():
    sns.jointplot(v1, v2, kind='hex')


def sns_style():
    # set the seaborn style for all the following plots
    sns.set_style('white')
    sns.jointplot(v1, v2, kind='kde', space=0)


def pairplot():
    sns.pairplot(iris, hue='Name', diag_kind='kde', size=2)


pairplot()

plt.show()
