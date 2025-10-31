import os
from time import sleep

path = input('Введи путь: ')
os.chdir(path)
lst = os.listdir()
dic = {}
inc = 1

for i in lst:
    if os.path.isfile(i) == True:
        continue
    else:
        lst.remove(i)

lst.sort(key=lambda t: os.stat(t).st_mtime)

size = len(lst)
print(size)

print('Будут Переименованы следующие файлы:')

for i in lst:
    name, ext = os.path.splitext(i)
    print(f"{i} -> {str(inc) + ext}")
    inc += 1

if  input('\nПродолжить?(Y/n): ').lower() == 'y':
    inc = 1
    for i in lst:
        name, ext = os.path.splitext(i)
        os.rename(i, (str(inc) + ext))
        inc += 1
    print('Файлы успешно переименованы!')
    sleep(1)
else:
    print("Программа завершила работу без внесения изменений")
    sleep(1)


# print('\nБудут переименованы эти файлы:')
#
# for key, value in pairs.items():
#     new_name = str(key) + value[-4:]
#     print(f'"{value}" -> "{new_name}"')
#
#
# if  input('\nПродолжить?(Y/n): ').lower() == 'y':
#     for key, value in pairs.items():
#         new_name = str(key) + value[-4:]
#         os.rename(value, new_name)
#     print('Файлы успешно переименованы!')
#     sleep(3)
# else: print("Программа завершила работу без внесения изменений")
# sleep(3)