# 画图
from turtle import *

# 设置画笔宽度
width(4)

n = 99
while(n > 0):
    # 前进
    forward(200)
    # 右转
    right(90)
    forward(200)

    # 笔刷颜色
    pencolor('red')
    right(90)
    forward(200)

    pencolor('green')
    right(90)
    forward(200)

    pencolor('yellow')
    right(90)
    forward(200)

    pencolor('blue')
    right(90)
    n -= 1


done()
