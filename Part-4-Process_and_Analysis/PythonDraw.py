#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle 
# 也可以from turtle import *之后不需要写turtle但是怕函数重名 
# 还可以import turtle as t  之后t.setup()
# 设置窗体大小及位置（宽，高，左上角位置坐标（x,y），默认正中心）
turtle.setup(650,350,200,200)
turtle.penup() # 或者pu，画笔抬起
turtle.forward(-250) #或者fd，负数表倒退
turtle.pendown()  # 或者pd，画笔落下
turtle.pensize(25)  # 或者width，画笔宽度
turtle.pencolor('purple')  #修改颜色，字符串、RGB小数值、RGB元组值都可以
turtle.seth(-40)    # 改变为绝对角度，海归角度为left&right
for i in range(4):
    turtle.circle(40,80)   #（半径，长度）
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
