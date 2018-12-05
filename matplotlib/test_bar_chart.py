import matplotlib.pyplot as plt


# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.bar.html
def bar_chart():
    x = [1, 2, 3]
    height = [10, 5, 20]
    plt.bar(x, height)
    plt.show(block=False)


# bar_chart()
