import os
path = input ('Введи путь: ')
os.chdir(path)
for i in os.listdir():
    num = i[-6:-4]
    ext = i[-3:]
    new_name = num + '.' + ext
    print (f'Старое имя: {i}\nНовое имя: {new_name}')

    os.rename(i, new_name)
print ('ОК!')