'''
作者:Egbert
功能：连续画多个五角星
版本：2.0
日期：2019-3-12
'''

'''
turtle库补充：
turtle.penup()
'''

import turtle
import math
def main():
    '''主函数'''

    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor('red')

    count = 1
    while count <= 30:
        forward = math.ceil(count / 5) * 50
        turtle.forward(forward)
        turtle.right(144)
        count =count + 1
    turtle.exitonclick()

if __name__ == '__main__':
    main()