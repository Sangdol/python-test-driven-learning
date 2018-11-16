import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# subplot with 1 row, 2 columns, and current axis is 1st subplot axes
plt.subplot(1, 2, 1)

linear_data = np.array([1,2,3,4,5,6,7,8])

plt.plot(linear_data, '-o')
plt.show()

plt.plot(linear_data ** 2, '-o')
plt.show()
