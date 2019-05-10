'''问题：输入一串数字，用列表保存。要求，输出列表中的最大值，并输出最大值的索引。
（1）可自定义列表长度
（2）列表中的元素，只能是数字，不是数字提示重新输入
（3）输入数字的范围在0-100之间，包括100和0

思考一下，若是有重复的数字，应该如何解决，如何统计重复的个数，有多少组重复的数字。'''

'''
作者：Egbert
功能：用列表保存输入的一串数字，并输出列表中的最大值及其索引。
新增：只能输入不大于100的数字，否则重新输入
版本：2.0
问题：无法识别负数，判断条件缺陷很大，只能是整数无法输入浮点数
时间：2019-3-31
'''

def main():
    store = []
    i = 'y'
    time = 0
    while i == 'y':
        store.append(input("请输入一个数字："))
        if store[time].isdigit():
            if int(store[time]) < 101:
                time += 1
                i = input("还想继续输入下一个数字吗（y/n)？")
            else:
                print("请输入不大于100的数字！")
                del store[time]
        else:
            print("输入的不是数字！")
            del store[time]

    print('您输入的列表长度为'+str(len(store))+'.\n')
    print('您输入数字中最大值为' + str(max(store)) + '.\n')
    print('您输入数字的最大值索引为' + str(store.index(max(store))) + '!\n')


if __name__ == '__main__':
    main()
