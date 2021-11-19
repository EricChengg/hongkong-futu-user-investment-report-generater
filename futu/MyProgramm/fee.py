import datetime
import math

import common

platformFees = 15  # 平台使用費
tradeSystemFee = 0.5  # 交易系統使用費
theExchangeTradeFee = 0.00005  # 交易所交易費%
newStampDuty = 0.0013  # 新印花稅%（2021年8月1日生效)
newStampDutyStartDate = datetime.datetime.strptime("2021-08-01", "%Y-%m-%d")
oldStampDuty = 0.001  # 舊印花稅%
SFCTransactionLevy = 0.000027  # 證監會交易徵費%
stock_settlement_fee = 0.00002  # 交收費 最少2元，最多100元


def get_order_price(price=0, qty=0):
    order_price = price * qty
    return round(order_price, 2)


def get_trade_fee(trade_record):
    stock_price = get_order_price(trade_record.price, trade_record.qty)
    trade_date = datetime.datetime.strptime(trade_record.create_time, common.openapi_datetime_format)
    total_cost = platformFees + tradeSystemFee + get_stamp_duty_cost(stock_price, trade_date) + get_sfc_transaction_levy_cost(stock_price) + get_exchange_trade_cost(stock_price) + get_stock_settlement_fee(stock_price)
    return round(total_cost, 2)


def get_exchange_trade_cost(stock_price):
    return round(stock_price * theExchangeTradeFee, 2)


def get_stamp_duty_cost(stock_price, trade_date):
    if trade_date > newStampDutyStartDate:
        return math.ceil(stock_price * newStampDuty)
    else:
        return math.ceil(stock_price * oldStampDuty)


def get_sfc_transaction_levy_cost(stock_price):
    return round(stock_price * SFCTransactionLevy, 2)


def get_stock_settlement_fee(stock_price):
    stock_settlement_fee_cost = stock_price * stock_settlement_fee
    if stock_settlement_fee_cost < 2:
        return 2
    elif stock_settlement_fee_cost > 100:
        return 100
    else:
        return round(stock_settlement_fee_cost, 2)
