#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import *
color('red','red')
begin_fill()   # 开始画
for i in range(5):
    fd(200)    # 向forward移动划线
    rt(144)    # 向right转144度
end_fill()     # 完成图片填充
done()
