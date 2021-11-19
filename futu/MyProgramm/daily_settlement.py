from datetime import datetime
import common
from trade_record import TradeRecord

daily_settlements_field = ['date', 'buy_count', 'buy_amount', 'buy_cost',
                           'total_buy_amount', 'sell_count', 'sell_amount', 'sell_cost',
                           'total_sell_amount', 'earn']


class DailySettlement:

    def __init__(self):
        self.date = ''
        self.buy_count = 0
        self.buy_amount = 0
        self.buy_cost = 0
        self.total_buy_amount = 0
        self.sell_count = 0
        self.sell_amount = 0
        self.sell_cost = 0
        self.total_sell_amount = 0
        self.earn = 0


def get_daily_settlement(trade_records) -> list:
    daily_settlements = []
    ds = DailySettlement()
    i = 1
    while i < len(trade_records):
        create_time = datetime.strptime(trade_records[i].create_time, common.openapi_datetime_format).\
            date().strftime(common.date_format)
        if ds.date == '':
            ds.date = create_time
        else:
            if ds.date != create_time:
                ds.earn = ds.total_sell_amount - ds.total_buy_amount
                ds.earn = round(ds.earn, 2)
                daily_settlements.append(ds.__dict__.values())
                ds = DailySettlement()
                ds.date = create_time
        if trade_records[i].trd_side == 'SELL':
            ds.sell_count += 1
            ds.sell_amount += trade_records[i].order_price
            ds.sell_cost += trade_records[i].cost
            ds.total_sell_amount += (trade_records[i].order_price + trade_records[i].cost)
        elif trade_records[i].trd_side == 'BUY':
            ds.buy_count += 1
            ds.buy_amount += trade_records[i].order_price
            ds.buy_cost += trade_records[i].cost
            ds.total_buy_amount += (trade_records[i].order_price + trade_records[i].cost)
        i += 1
    print('daily settlements done')
    return daily_settlements
