import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def animate():
    n = 100
    x = np.random.randn(n)
    plt.ion()

    # create the function that will do the plotting, where curr is the current frame
    def update(curr):
        # check if animation is at the last frame, and if so, stop the animation a
        print(curr)
        if curr == n:
            a.event_source.stop()
        plt.cla()
        bins = np.arange(-4, 4, 0.5)
        plt.hist(x[:curr], bins=bins)
        plt.axis([-4, 4, 0, 30])  # hard-coded to avoid auto-scaling
        plt.gca().set_title('Sampling the Normal Distribution')
        plt.gca().set_ylabel('Frequency')
        plt.gca().set_xlabel('Value')
        plt.annotate('n = {}'.format(curr), [3, 27])

    fig = plt.figure()
    # Not working in Scientific Mode
    a = animation.FuncAnimation(fig, update, interval=100)


animate()
