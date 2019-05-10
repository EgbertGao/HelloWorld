'''
作者:Egbert
功能：画一个五角星
版本：1.0
日期：2019-3-12
'''
import turtle
def main():
    '''主函数'''
    count = 1
    while count <= 5:
        turtle.forward(100)
        turtle.right(144)
        count = count + 1
    turtle.extionclick()

if __name__ == '__main__':
    main()
