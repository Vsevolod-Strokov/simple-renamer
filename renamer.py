import os

path = input('Введи путь: ')
os.chdir(path)
lst = os.listdir()
dic = {}

def is_folder(folder):  # - Проверка является ли объект папкой
    for i in folder:
        if i == '.':
            return False
            break

for i in lst:
    if is_folder(i) == False:
        num = int(i[-6:-4])
        dic[num] = i
    else:
        continue

pairs = dict(sorted(dic.items()))

print('\nБудут переименованы эти файлы:')

for key, value in pairs.items():
    new_name = str(key) + value[-4:]
    print(f'"{value}" -> "{new_name}"')


if  input('\nПродолжить?(Y/n): ').lower() == 'y':
    for key, value in pairs.items():
        new_name = str(key) + value[-4:]
        os.rename(value, new_name)
    print('Файлы успешно переименованы!')
else: print("Программа завершила работу без внесения изменений")