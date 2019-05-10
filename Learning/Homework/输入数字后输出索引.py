'''
作者：Egbert
功能：用列表保存输入的一串数字，并输出列表中的最大值及其索引。
版本：1.0
时间：2019-3-19
'''

def main():
    store = []
    i = 'Y'
    while i == 'Y':
        store.append(input("请输入一个数字："))
        i = input("还想继续输入下一个数字吗（Y/N)？")
    print('您输入数字中最大值为'+ str(max(store)) + '.\n')
    print('您输入数字的最大值索引为' + str(store.index(max(store))) + '!\n')

if __name__ == '__main__':
    main()