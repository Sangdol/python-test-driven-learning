#
# applied-data-science-with-python/course2_downloads/Week4.ipynb
#
# pd.tools.plotting is deprecated -> pd.plotting
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris_raw = load_iris()
names = pd.Series(map(lambda i: iris_raw.target_names[i], iris_raw.target))
iris = pd.DataFrame(data=np.c_[iris_raw.data, names],
                    columns=(iris_raw.feature_names + ['Name']))


pd.plotting.scatter_matrix(iris)

pd.plotting.parallel_coordinates(iris, 'Name')

plt.show()
