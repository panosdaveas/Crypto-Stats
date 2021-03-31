import matplotlib.pyplot as plt
import numpy as np

from Math import Trade


class SnappingCursor:

    def __init__(self, ax, line, minY_value, xpoints, trade_id, trade):
        self.xpoints = xpoints
        self.ax = ax
        self.horizontal_line = ax.axhline(y=minY_value, color='k', lw=0.5, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.5, ls='--')
        self.x, self.y = line.get_data()
        self._last_index = None
        self.trade = trade
        if self.trade is not None:
            self.current_price = ax.axhline(trade.current_price, color='green', lw=0.5,
                                            ls='--')
            if trade.percentage < 0:
                self.current_price = ax.axhline(trade.current_price, color='red',
                                                lw=0.5, ls='--')
            self.trade_value = trade.trade_open
            self.trade_id = trade_id
            self.percentage = trade.percentage
        # text location in axes coords
        self.text = ax.text(0.25, 0.5, '', transform=ax.transAxes, alpha=0.5)

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(False)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        if self.trade is not None:
            self.current_price.set_visible(visible)
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
            if self.trade is not None:
                if self.trade_value - 100 <= event.ydata <= self.trade_value + 100:
                    self.text.set_text('open_trade @ %1.2f  p/l %1.2f %%' % (
                        self.trade_value, self.percentage))
            self.ax.figure.canvas.draw()


def plot_function(results, trade):
    #plt.style.use('dark_background')
    listDates = []
    listPrices = []
    marks = []
    mark_x = []
    mark_y = []
    trade_id = 0
    for i, document in enumerate(results, start=0):
        listDates.append(document['date'])
        listPrices.append(document['price'])
        if trade is not None:
            if document['price'] == trade[0]:
                trade_id = i
        if 'buy' in document:
            marks.append(document)
            mark_y.append(document['price'])
            mark_x.append(i)

    fig, ax = plt.subplots()
    trades_x = np.array(mark_x)
    trades_y = np.array(mark_y)
    xpoints = np.array(listDates)
    ypoints = np.array(listPrices)
    x = np.arange(len(xpoints))
    line, = plt.plot(x, ypoints, linewidth=0.6, label='current', zorder=1)
    plt.fill_between(x, ypoints.min(), ypoints, alpha=.1)
    plt.grid(axis='y', linestyle='dotted', linewidth=0.5)
    plt.xticks([])
    snap_cursor = SnappingCursor(ax, line, ypoints.min(), xpoints, trade_id, trade)
    fig.canvas.mpl_connect('motion_notify_event', snap_cursor.on_mouse_move)
    if trade is not None:
        plt.axhline(trade.trade_open, color='blue', linestyle='--', linewidth=0.5,
                    label='purchased')
        #if trade.buy:
        #    plt.scatter(trade_id, trade[0], marker='+', color='g')
        #else:
        #    plt.scatter(trade_id, trade[0], marker='+', color='r')

    for i, mark in enumerate(marks, start=0):
        if mark['buy'] is True:
            plt .scatter(trades_x[i], trades_y[i], marker='+', color='g', zorder=2)
        else:
            plt.scatter(trades_x[i], trades_y[i], marker='+', color='r', zorder=2)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_function(results=list, trade=Trade)
