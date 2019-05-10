'''
    作者：Egbert
    功能：实现一种汇率兑换
    日期：2019-3-9
    版本号：1.0
    增加功能：

'''


USD_VS_RMB = 6.77

currency_str_value = input('请输入货币金额（CNY or USD）：')

unit = currency_str_value[-3:]

if unit == 'CNY':
    rmb_str_value = currency_str_value[:-3]
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / USD_VS_RMB
    print('美元（USD）金额是：',usd_value)
elif unit == 'USD':
    rmb_str_value = currency_str_value[:-3]
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value / USD_VS_RMB
    print('人民币（RMB）金额是：',usd_value)