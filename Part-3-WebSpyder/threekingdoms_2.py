#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 提前将txt保存为utf-8编码
import jieba 
txt = open("D:/Vina_test/threekingdoms.txt","r",encoding="utf-8").read()  # 读取txt数据
excludes ={"将军","却说","荆州","二人","不可","不可","不能","如此","左右","如何","商议","军士",'军马'}
words = jieba.lcut(txt)
counts={}
for word in words:
    if len(word) == 1:
        continue
    elif word =="诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公"  or word == "云长":
        rword = "关羽"
    elif word == "孟德"  or word == "丞相":
        rword = "曹操"
    elif word == "玄德"  or word == "玄德曰":
        rword = "刘备"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) +1
for word in excludes:
    del counts[word]
items = list(counts.items())  # 构造中文单词的列表
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
