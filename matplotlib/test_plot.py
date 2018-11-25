import matplotlib.pyplot as plt
import numpy as np


# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
def test_basic_plot():
    lines = plt.plot(1, 3)
    assert len(lines) == 1

    default_line = lines[0]
    assert default_line.get_linestyle() == '-'  # Default line style
    assert default_line.get_data() == ([1], [3])
    assert default_line.get_color() == '#9467bd'
    assert default_line.get_marker() == 'None'

    # fmt = '[color][marker][line]'
    lines = plt.plot(1, 3, '.')

    marker_line = lines[0]
    assert marker_line.get_linestyle() == 'None'
    assert marker_line.get_data() == ([1], [3])
    assert marker_line.get_color() == '#8c564b'
    assert marker_line.get_marker() == '.'
