import math
from typing import Type
from datetime import datetime
import common
from futu import *
from prettytable import PrettyTable
import fee


class TradeRecord:
    def __init__(self, deal_id, trd_side, order_id, code, stock_name, qty, price, create_time,
                 counter_broker_id, counter_broker_name, status, order_price, cost):
        self.deal_id = deal_id
        self.trd_side = trd_side
        self.order_id = order_id
        self.code = code
        self.stock_name = stock_name
        self.qty = qty
        self.price = price
        self.create_time = create_time
        self.counter_broker_id = counter_broker_id
        self.counter_broker_name = counter_broker_name
        self.status = status
        self.order_price = order_price
        self.cost = cost


def get_trade_record(start_date, end_date) -> (list, list, list):
    trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111,
                                  security_firm=SecurityFirm.FUTUSECURITIES)
    print('start_date : ', start_date)
    print('end_date : ', end_date)
    ret, data = trd_ctx.history_deal_list_query(start=start_date, end=end_date)
    if ret == RET_OK:
        # lt = data.values.tolist()
        if data.shape[0] > 0:  # 如果成交列表不为空, null is no trade
            i = 0
            fields = ['deal_id', 'trd_side', 'order_id', 'code', 'stock_name', 'qty', 'price', 'create_time',
                      'counter_broker_id', 'counter_broker_name', 'status', 'order_price', 'cost']
            # t = PrettyTable(fields)
            trade_record_list = []
            trade_records = [TradeRecord]
            while i < len(data):
                tr = TradeRecord(data['deal_id'][i], data['trd_side'][i],
                                 data['order_id'][i], data['code'][i],
                                 data['stock_name'][i], round(data['qty'][i]),
                                 round(data['price'][i], 2), data['create_time'][i],
                                 data['counter_broker_id'][i],
                                 data['counter_broker_name'][i],
                                 data['status'][i],
                                 fee.get_order_price(data['price'][i], data['qty'][i]),
                                 fee.get_trade_fee(data.loc[i]))
                trade_record_list.append(tr.__dict__.values())
                trade_records.append(tr)
                i = i + 1
            # print(t)
            return fields, trade_record_list, trade_records
    else:
        print('history_deal_list_query error: ', data)
    trd_ctx.close()
