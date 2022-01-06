import common
from futu import *

position_stocks_field = ['code', 'position_side', 'stock_name', 'qty',
                        'nominal_price', 'cost_price', 'market_val',
                        'pl_ratio', 'pl_val', 'position_ratio(%)', 'total_assets']


class PositionStock:
    def __init__(self, code, position_side, stock_name, qty, nominal_price, cost_price, market_val, pl_ratio, pl_val,
                 position_ratio, total_assets):
        self.code = code
        self.position_side = position_side
        self.stock_name = stock_name
        self.qty = qty
        self.nominal_price = nominal_price
        self.cost_price = cost_price
        self.market_val = market_val
        self.pl_ratio = pl_ratio
        self.pl_val = pl_val
        self.position_ratio = position_ratio
        self.total_assets = total_assets


def cal_position_ratio(pl_ratio=0, total_assets=0):
    return round((pl_ratio / total_assets) * 100, 2)


def get_position_stock() -> list:
    trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111,
                                  security_firm=SecurityFirm.FUTUSECURITIES)
    ret, data = trd_ctx.accinfo_query()
    total_assets = data['total_assets'][0]
    ret, data = trd_ctx.position_list_query()

    position_stocks = []
    i = 0
    while i < len(data):
        ps = PositionStock(data['code'][i], data['position_side'][i], data['stock_name'][i],
                           data['qty'][i], data['nominal_price'][i], data['cost_price'][i],
                           data['market_val'][i], data['pl_ratio'][i], data['pl_val'][i],
                           cal_position_ratio(data['market_val'][i], total_assets), total_assets)
        i = i + 1
        position_stocks.append(ps.__dict__.values())

    trd_ctx.close()
    return position_stocks
#/Users/ericcheng/Downloads/futu-user-investment-report-generater/futu/MyProgramm/position_stock.py
