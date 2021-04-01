from typing import NamedTuple


# struct-like
class Trade(NamedTuple):
    trade_open: float
    current_price: float
    percentage: float
    profit: float
    buy: bool


def percent_diff(a, b):
    return ((a - b) / b) * 100


def price_calculator(last_entry, last_open_trade):
    if len(last_open_trade) != 0:
        trade_open_value = last_open_trade[0]['price']
        current_price = last_entry[0]['price']
        percentage = percent_diff(current_price, trade_open_value)
        profit = current_price - trade_open_value
        buy = last_open_trade[0]['buy']
        trade = Trade(trade_open_value, current_price, percentage, profit, buy)
        return trade
    else:
        return None


def alert_open(results, last_trade):
    a = results[len(results) - 1]['price']
    b = results[len(results) - 2]['price']
    c = results[len(results) - 3]['price']
    if len(last_trade) == 0 or last_trade[0]['buy'] is False:
        if percent_diff(b, c) < 0:
            if percent_diff(a, b) >= 0.1:
                print("buy")
                return True


def alert_close(results, last_trade):
    a = results[len(results) - 1]['price']
    b = results[len(results) - 2]['price']
    c = results[len(results) - 3]['price']
    if len(last_trade) != 0 and last_trade[0]['buy'] is True:
        d = last_trade[0]['price']
        if percent_diff(a, d) > 0:
            if percent_diff(a, b) <= -0.1:
                print('sell')
                return True


if __name__ == '__main__':
    price_calculator(last_entry=list, last_open_trade=list)
    alert_open(results=list, last_trade=list)
