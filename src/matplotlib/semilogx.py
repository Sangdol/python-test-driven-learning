import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.semilogx.html
plt.figure()
gamma = np.logspace(-4, 1, 6)
plt.semilogx(gamma, range(6), label='training scores')
plt.semilogx(gamma, range(1, 12, 2), label='test scores')
plt.legend(loc=4)
plt.show()
