'''
#7-1 汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息
car = input('Which car do you want to rent?')
print('Let me see if I can find you a ' + car.title() + '.\n')

#7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，没有空桌；
reservation_num = input("How many people will be attended in tonight's dinner?")
if int(reservation_num) > 8:
    print('Sorry, there is no avaliable sities.')
else :
    print('Restaurant has already reserved a table for you!')

#7-3 10的整数倍：让用户输入一个数字，并指出这个数字是否是10的整数倍
get_num = input("Please enter a number, "
                "then I'll tell you 10 can be divided exactly by this number:")
if int(get_num) % 10 == 0:
    print('10 can be divided exactly by ' + str(get_num) + '.\n')
else :
    print('10 can not be divided exactly by ' + str(get_num) + '.\n')


#7-4 比萨配料： 编写循环，提示用户输入一系列配料，并在用户输入‘quit’时结束。
#每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料

while True:
    get_str = input('Please add an ingredient that you want:')
    if get_str != 'quit':
        print('We have already added ' + get_str + ' in the Pizza!')
    else:
        break


#7-5 电影票：电影院根据年龄收取票价——不到3岁免票；3-12岁10美元；超过12岁15美元。
# 循环，询问年龄并指出票价(为啥加入退出流程后无法使用)

# 设置一个标志
active = True

while active:
    adult_age = input('How old are you? ')

    adult_age = int(adult_age)
    if adult_age > 12:
        print('Your ticket price is $15.')
    elif adult_age > 3:
        print('Your ticket price is $10.')
    else :
        print('Free!')

    #判断是否退出
    judge_sentence = input('Do you want to quit? ')
    if judge_sentence == 'quit':
        active = False


#7-8 熟食店：创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；
# 再创建一个名为finished_sandwiches的空列表，对于其中的每种三明治，都打印一条消息，
# 并将其已到列表finished_sandwiches.所有三明治都做好后，打印一条消息将这些三明治列出来。

sandwich_orders = ['tuna sandwich', 'egg sandwich', 'vegetable sandwich']
finished_sandwiches = []

while sandwich_orders :
    get_sandwich = sandwich_orders.pop()
    print('We have {}.'.format(get_sandwich))
    finished_sandwiches.append(get_sandwich)

print('\nAll the sandwich has been prepared!')


#7-9 移除pastrami并告知已售完
sandwich_orders = ['tuna sandwich', 'pastrami', 'egg sandwich', 'pastrami', 'vegetable sandwich', 'pastrami']
print(sandwich_orders)
print('Pastrami has been sold out!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
'''
