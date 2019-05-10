'''
# 10-1-1 打印时读取整个文件
filename = 'learning_python.txt'

with open(filename) as file_object:
    file = file_object.read()
    print(file)

# 10-1-2 打印时遍历文件对象

filename = 'learning_python.txt'
i = 0

with open(filename) as file_object:
    while i < 3:
        line = file_object.readline()
        print(line)
        i += 1


#10-1-3 在with代码块外打印
filename = 'learning_python.txt'
i = 0
lines = []

with open(filename) as file_object:
    while i < 3:
        line = file_object.readline()
        lines.append(line)
        i += 1

for sen in lines:
    print(sen)

#10-3

name = input('请输入你的名字：')

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write("This guest's name is {}.".format(name))
'''

