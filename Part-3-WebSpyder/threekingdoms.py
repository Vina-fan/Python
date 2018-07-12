#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 提前将txt保存为utf-8编码
import jieba 
txt = open("D:/Vina_test/threekingdoms.txt","r",encoding="utf-8").read()  # 读取txt数据
words = jieba.lcut(txt)
counts={}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) +1
items = list(counts.items())  # 构造中文单词的列表
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
