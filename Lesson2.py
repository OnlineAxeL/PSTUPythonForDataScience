# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:04:04 2020

@author: Aleksey
"""

#импортируем библиотеку нампи
import numpy as np

#закидываем данные из csv файла в переменную
array = np.genfromtxt('lesson2.csv', delimiter=';', names=True)

#объявляем необходимые нам для цикла убого названные переменные
max = 0
maxi = -1
maxj = -1
min = 100
mini = -1
minj = -1

#в цикле ищем минимум и максимум в нашем массиве
for i in range(0, 9):
    for j in range(0, 9):
        if array[i][j] > max:
            max = array[i][j]
            maxi = i
            maxj = j
        if array[i][j] < min:
            min = array[i][j]
            mini = i
            minj = j

#печатаем массив, максимум и минимум с индексами, потом меняем местами и выводим снова для сравнения
print(array)
print(max, maxi, maxj)
print(min, mini, minj)
array[maxi][maxj] = min
array[mini][minj] = max

print(array)