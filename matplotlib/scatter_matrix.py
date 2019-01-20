import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from pandas.plotting import scatter_matrix

# https://stackoverflow.com/questions/21131707/multiple-data-in-scatter-matrix
iris = load_iris()
iris_data = pd.DataFrame(data=iris['data'],columns=iris['feature_names'])
iris_data["target"] = iris['target']

color_wheel = {1: "#0392cf",
               2: "#7bc043",
               3: "#ee4035"}
colors = iris_data["target"].map(lambda x: color_wheel.get(x + 1))
ax = scatter_matrix(iris_data, color=colors, alpha=0.6, figsize=(15, 15), diagonal='hist')
plt.show()
