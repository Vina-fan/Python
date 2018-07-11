#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
scale = 10
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()# 计时
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,"-"))




# 单行动态刷新,由于Idle是开发环境（不用），需要用双击或控制台运行
import time
for i in range(101):
    print("\r{:3}%".format(i),end="") # \r使光标退回行首，end=""不换行，光标停留在该行后面
    time.sleep(0.1)
