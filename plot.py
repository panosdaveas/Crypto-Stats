import matplotlib.pyplot as plt
import numpy as np
import pymongo


class SnappingCursor:

    def __init__(self, ax, line, minY_value, xpoints):
        self.xpoints = xpoints
        self.ax = ax
        self.horizontal_line = ax.axhline(y=minY_value, color='k', lw=0.5, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.5, ls='--')
        self.x, self.y = line.get_data()
        self._last_index = None
        # text location in axes coords
        self.text = ax.text(0.25, 0.5, '', transform=ax.transAxes, alpha=0.5)

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(False)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw

    def on_mouse_move(self, event):
        if not event.inaxes:
            self._last_index = None
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.draw()
        else:
            self.set_cross_hair_visible(True)
            x, y = event.xdata, event.ydata
            index = min(np.searchsorted(self.x, x), len(self.x) - 1)
            if index == self._last_index:
                return  # still on the same data point. Nothing to do.
            self._last_index = index
            x = self.x[index]
            y = self.y[index]
            # update the line positions
            self.horizontal_line.set_ydata(y)
            self.vertical_line.set_xdata(x)
            self.text.set_text('%1.2f, %s' % (y, self.xpoints[x]))
            self.ax.figure.canvas.draw()


def plot_function(results, purchases):

    listDates = []
    listPrices = []

    for document in results:
        listDates.append(document['date'])
        listPrices.append(document['price'])

    last = purchases[0]

    fig, ax = plt.subplots()
    xpoints = np.array(listDates)
    ypoints = np.array(listPrices)
    x = np.arange(len(xpoints))
    line, = plt.plot(x, ypoints, linewidth=0.6, label='current')
    plt.grid(axis='y', linestyle='dotted', linewidth=0.5)
    plt.axhline(last['price'], color='r', linestyle='--', linewidth=0.5, label='purchased')
    plt.xticks([])
    plt.fill_between(x, ypoints.min(), ypoints, alpha=.1)
    snap_cursor = SnappingCursor(ax, line, ypoints.min(), xpoints)
    fig.canvas.mpl_connect('motion_notify_event', snap_cursor.on_mouse_move)
    plt.show()


if __name__ == '__main__':
    plot_function(results=pymongo.cursor.Cursor, purchases=pymongo.cursor.Cursor)
