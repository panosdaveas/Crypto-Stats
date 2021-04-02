def percent_diff(a, b):
    return ((a - b) / b) * 100


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
    alert_open(results=list, last_trade=list)
    alert_close(results=list, last_trade=list)
