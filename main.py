"""
Задание: Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
В качестве выполненного ДЗ отправить файл с расширением .py в котором будет находится код программы.
"""
import random

a = [random.randint(0, 10) for i in range(0, 10)]
b = [random.randint(0, 10) for i in range(0, 10)]
result = []
for i in a:
    if (i not in b) and (i not in result):
        result.append(i)
print(a)
print(b)
print(result)

