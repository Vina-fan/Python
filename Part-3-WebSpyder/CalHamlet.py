def getText():
    txt = open("D:/Vina_test/hamlet.txt","r").read()  # 读取txt数据
    txt = txt.lower()
    for ch in "!'#$%()*<+_>?/@[\\]{}^&~|\‘’":
        txt = txt.replace(ch," ")  # 替换乱码
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) +1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse = True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
