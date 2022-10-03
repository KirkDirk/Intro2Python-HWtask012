# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

# создание, наполнение и перемешивание начального списка
sizelist = int(input('Введите размер списка: '))
somelist = []
for i in range(sizelist):
    somelist.append(i)
random.shuffle(somelist)
print(somelist)

# формирование списка из перемноженных пар
compositionlist = []
for i in range(sizelist//2):
    compositionlist.append(somelist[i]*somelist[-i-1])
if (sizelist % 2 == 1): compositionlist.append(somelist[sizelist//2])
print(compositionlist)