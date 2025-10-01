import os
path = input ('Введи путь: ')
os.chdir(path)
lst = os.listdir()
dic = {}

for i in lst:
    num = int(i[-6:-4])
    dic[num] = i

pairs = dict(sorted(dic.items()))

for key,value in pairs.items():
    new_name = str(key) + value[-4:]
    os.rename(value, new_name)
    
print ('ОК!')