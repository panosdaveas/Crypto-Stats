from typing import NamedTuple


# struct-like
class Trade(NamedTuple):
    trade_open: float
    current_price: float
    percentage: float
    profit: float


def percent_diff(a, b):
    return ((a - b) / b) * 100


def price_calculator(results, last_trade):
    if len(last_trade) != 0:
        trade_open_value = last_trade[0]['price']
        current_price = results[len(results) - 1]['price']
        percentage = percent_diff(current_price, trade_open_value)
        profit = current_price - trade_open_value
        trade = Trade(trade_open_value, current_price, percentage, profit)
        return trade
    else:
        return None


if __name__ == '__main__':
    price_calculator(results=list, last_trade=list)
