import matplotlib.pyplot as plt
import numpy as np


def plot_function(listDates, listPrices):
    xpoints = np.array(listDates)
    ypoints = np.array(listPrices)
    x = np.arange(len(xpoints))
    plt.plot(x, ypoints, linewidth=0.6, label='current')
    plt.grid(axis='y', linestyle='dotted', linewidth=0.5)
    plt.axhline(y=54320, color='r', linestyle='--', linewidth=0.5, label='purchased')
    plt.xticks([])
    plt.fill_between(x, ypoints.min(), ypoints, alpha=.1)
    plt.show()


if __name__ == '__main__':
    plot_function(listDates=list, listPrices=list)
