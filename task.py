import csv

with open('source.csv', 'r', encoding='utf-8') as f:
    l = f.readlines()
    print(type(l))
    print(l)

word =input("鬼滅の登場人物の名前を入力してください >>> ")
if word in l:
    print('存在します')
else:
    l.append(word)
print(l)
    
