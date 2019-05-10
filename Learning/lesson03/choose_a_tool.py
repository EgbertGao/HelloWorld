'''
    作者：Egbert
    功能：52周存钱挑战
    版本：5.0
    日期：2019-4-26
    2.0新增功能：记录每周的存款数
    3.0新增功能：使用循环直接计数
    4.0:可以用户输入存入金额及递增金额、周数等，并封装成函数
    5.0：根据用户输入的日期，判断是一年中的第几周，然后输出相应的存款金额
    根据用户选择3个工具调用相应的 工具提供给用户使用
'''

import math
import datetime

def save_money_in_n_week(money_per_week, increase_money, total_week):
    money_list = []  # 记录每周存款数的列表
    saved_money_list = [] #记录每周账户累计


    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)

        money_per_week += increase_money
    return saved_money_list

def main():
    # 主函数
    money_per_week = float(input('请输入每周的存入金额：'))  # 每周存入的金额
    i = 1  # 记录周数
    increase_money = float(input('请输入每周递增的金额：'))  # 递增的金额
    total_week = int(input('请输入总共的周数：'))  # 总共的周数
    saving = 0  # 账户累计，局部变量
    saved_money_list = save_money_in_n_week(money_per_week, increase_money, total_week)

    input_date_str = input('请输入日期（yyyy/mm/dd):')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    week_number = input_date.isocalendar()[1]

    print('第{}周的存款为{}'.format(week_number, saved_money_list[week_number-1]))

if __name__ == '__main__':
    main()
