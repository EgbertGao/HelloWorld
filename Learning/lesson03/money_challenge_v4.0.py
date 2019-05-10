'''
    作者：Egbert
    功能：52周存钱挑战
    版本：4.0
    日期：2019-4-26
    2.0新增功能：记录每周的存款数
    3.0新增功能：使用循环直接计数
    4.0:可以用户输入存入金额及递增金额、周数等，并封装成函数
'''

import math

def save_money_in_n_week(money_per_week, increase_money, total_week):
    money_list = []  # 记录每周存款数的列表

    # while i <= total_week:
    for i in range(total_week):
        # #存钱操作
        # saving += money_per_week
        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        print('第{}周，存入{}元，账户累计{}元。'.format(i + 1, money_per_week, saving))

        # 更新下一周的存钱金额
        money_per_week += increase_money
    return saving

def main():
    # 主函数
    money_per_week = float(input('请输入每周的存入金额：'))  # 每周存入的金额
    i = 1  # 记录周数
    increase_money = float(input('请输入每周递增的金额：'))  # 递增的金额
    total_week = int(input('请输入总共的周数：'))  # 总共的周数
    saving = 0  # 账户累计，局部变量
    saving = save_money_in_n_week(money_per_week, increase_money, total_week)
    print('总存款金额',saving)

if __name__ == '__main__':
    main()
