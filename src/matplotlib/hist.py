"""

From "Applied Plotting, Charting & Data Representation in Python"

"""

import matplotlib.pyplot as plt
import numpy as np

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000) + 7
x4 = np.random.uniform(14, 20, 10000)

# plot the histograms
plt.figure(figsize=(9, 3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5)
plt.axis([-7, 21, 0, 0.6])

plt.text(x1.mean() - 1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean() - 1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean() - 1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean() - 1.5, 0.5, 'x4\nUniform')

plt.show()
