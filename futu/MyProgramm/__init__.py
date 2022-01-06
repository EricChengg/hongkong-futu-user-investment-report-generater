from datetime import datetime
import csv_editor

csv_editor.write_trade_record_report(start_date='2019-01-03')
exit()

#
# from futu import *

# trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
# data['total_assets'][0]
# ret, data = trd_ctx.accinfo_query()
# trd_ctx.close()
# if ret == RET_OK:
#     print(data)
#     print(data['power'][0])  # 取第一行的购买力
#     print(data['power'].values.tolist())  # 转为 list
#     print(data['cash'][0])
#     print(data['total_assets'][0])
# else:
#     print('accinfo_query error: ', data)
# trd_ctx.close()  # 关闭当条连接


# quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
#
# ret, data = quote_ctx.get_capital_flow("HK.00700")
# if ret == RET_OK:
#     print(data)
#     # print(data['in_flow'][0])    # 取第一条的净流入的资金额度
#     # print(data['in_flow'].values.tolist())   # 转为 list
#     # print(data['in_flow'].values.tolist())
#     # for d in data:
#     #     print("data : ", )
# else:
#     print('error:', data)
# quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
