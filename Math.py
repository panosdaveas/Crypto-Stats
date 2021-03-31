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


def price_calculator(results, last_trade):
    if len(last_trade) != 0:
        trade_open_value = last_trade[0]['price']
        current_price = results[len(results) - 1]['price']
        percentage = percent_diff(current_price, trade_open_value)
        profit = current_price - trade_open_value
        buy = last_trade[0]['buy']
        trade = Trade(trade_open_value, current_price, percentage, profit, buy)
        return trade
    else:
        return None


def alert(results, last_trade):
    a = results[len(results) - 1]['price']
    b = results[len(results) - 2]['price']
    c = results[len(results) - 3]['price']
    d = last_trade[0]['price']
    if last_trade[0]['buy'] is False:
        if percent_diff(b, c) < 0:
            if percent_diff(a, b) >= .2:
                print("buy")
                return True
    elif last_trade[0]['buy'] is True:
        if percent_diff(a, d) > 0:
            if percent_diff(a, b) <= -.2:
                print('sell')
                return False
    print('None')
    return None


if __name__ == '__main__':
    price_calculator(results=list, last_trade=list)
    alert(results=list, last_trade=list)
