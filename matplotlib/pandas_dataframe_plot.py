#
# applied-data-science-with-python/course2_downloads/Week4.ipynb
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# see the pre-defined styles provided.
# print(plt.style.available)
plt.style.use('seaborn-colorblind')

np.random.seed(123)

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20},
                  index=pd.date_range('1/1/2017', periods=365))


# df.plot()
# df.plot('A', 'B', kind='scatter')

# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
# df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')

# equal aspect
# ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
# ax.set_aspect('equal')

# df.plot.box()

# df.plot.hist(alpha=0.7)

# df.plot.kde()


plt.show()
