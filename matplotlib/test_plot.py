import matplotlib.pyplot as plt
import pytest


def setup_function():
    plt.figure()


def teardown_function():
    plt.clf()


# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
def test_basic_plot():
    lines = plt.plot(1, 3)
    assert len(lines) == 1

    default_line = lines[0]
    assert default_line.get_linestyle() == '-'  # Default line style
    assert default_line.get_data() == ([1], [3])
    assert default_line.get_marker() == 'None'

    # fmt = '[color][marker][line]'
    lines = plt.plot(1, 3, '.')

    marker_line = lines[0]
    assert marker_line.get_linestyle() == 'None'
    assert marker_line.get_data() == ([1], [3])
    assert marker_line.get_marker() == '.'


# https://matplotlib.org/api/backend_agg_api.html
@pytest.mark.skip(reason="Nothing to test. Just a code sample.")
def test_plot_without_scripting_layer():
    # First let's set the backend without using mpl.use() from the scripting layer
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure

    # create a new figure
    fig = Figure()

    # associate fig with the backend
    canvas = FigureCanvasAgg(fig)

    # add a subplot to the fig
    ax = fig.add_subplot(111)

    # plot the point (3,2)
    ax.plot(3, 2, '.')

    # save the figure to test.png
    # you can see this figure in your Jupyter workspace afterwards by going to
    # https://hub.coursera-notebooks.org/
    canvas.print_png('test.png')


# https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.axis.html
def test_axis():
    # plot the point (3,2) using the circle marker
    plt.plot(3, 2, 'o')

    # get the current axes
    ax = plt.gca()
    # Not always the same
    # assert ax.axis() == (2.835, 3.165, 1.89, 2.1100000000000003)

    # Set axis properties [xmin, xmax, ymin, ymax]
    ax.axis([0, 6, 0, 10])
    assert ax.axis() == (0, 6, 0, 10)

    artists = ax.get_children()

    assert len(artists) == 11
    assert list(map(lambda a: str(type(a)), artists)) == [
        "<class 'matplotlib.lines.Line2D'>",
        "<class 'matplotlib.spines.Spine'>",
        "<class 'matplotlib.spines.Spine'>",
        "<class 'matplotlib.spines.Spine'>",
        "<class 'matplotlib.spines.Spine'>",
        "<class 'matplotlib.axis.XAxis'>",
        "<class 'matplotlib.axis.YAxis'>",
        "<class 'matplotlib.text.Text'>",
        "<class 'matplotlib.text.Text'>",
        "<class 'matplotlib.text.Text'>",
        "<class 'matplotlib.patches.Rectangle'>"]
