"""Visualize the distribution of different samples."""

import pandas as pd
import matplotlib.pyplot as plt


def plot_histogram(sample, title, bins=3, **kwargs):
    """Plot the histogram of a given sample of random values.

    Parameters
    ----------
    sample : pandas.Series
        raw values to build histogram
    title : str
        plot title/header
    bins : int
        number of bins in the histogram
    kwargs : dict
        any other keyword arguments for plotting (optional)
    """
    # TODO: Plot histogram

    # TODO: show the plot
    # df = pd.DataFrame({
    # 'length': [1.5, 0.5, 1.2, 0.9, 3],
    # 'width': [0.7, 0.2, 0.15, 0.2, 1.1]
    # }, index = ['pig', 'rabbit', 'duck', 'chicken', 'horse'])
    # hist = df.hist(bins=3)
    return sample.hist(bins =bins)


def test_run():
    """Test run plot_histogram() with different samples."""
    # Load and plot histograms of each sample
    # Note: Try plotting them one by one if it's taking too long
    A = pd.read_csv("eod-quotemedia.csv", header=None, squeeze=True)
    plot_histogram(A, title="Sample A")

    # B = pd.read_csv("B.csv", header=None, squeeze=True)
    # plot_histogram(B, title="Sample B")
    #
    # C = pd.read_csv("C.csv", header=None, squeeze=True)
    # plot_histogram(C, title="Sample C")
    #
    # D = pd.read_csv("D.csv", header=None, squeeze=True)
    # plot_histogram(D, title="Sample D")
    # df = pd.DataFrame({
    #     'length': [1.5, 0.5, 1.2, 0.9, 3],
    #     'width': [0.7, 0.2, 0.15, 0.2, 1.1]
    # }, index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
    # hist = df.hist(bins=3)
    plt.show()


if __name__ == '__main__':
    test_run()