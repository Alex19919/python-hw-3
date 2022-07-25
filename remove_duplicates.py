# Завдання 3
# Файл: remove_duplicates.py Оцінка: 25
# Створіть функцію def remove_duplicates(array) яка приймає цілочисельний масив, відсортований у порядку зростання, видаліть дублікати чисел, щоб кожен унікальний елемент з’являвся лише один раз. Функція має повертати новий масив без дуплікатів чисел, відносний порядок елементів має бути незмінним
# Тестувати функцію ви можете як завгодно: за допомогою модуля sys і аргументів програми, або за допомогою input() або в результаті викликів функції. Але в файлі remove_duplicates.py повина бути створена функція def remove_duplicates(array) яка виконує необхідну логіку.
# Приклади:
# remove_duplicates([1, 1, 2]) -> [1, 2]
# remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) -> [0, 1, 2, 3, 4]
# remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1]) -> [1]

import sys

def remove_duplicates(array):
	if len(array) == 0:
		print ("Array")
		sys.exit()
	list = []
	list.append(array[0])
	for i in range(1, len(array)):
		try:
			if int(array[i]) < int(array[i-1]):
				print ('Invalid list: not sorted')
				sys.exit()
			if int(array[i]) != int(array[i-1]):
				list.append(array[i])
		except ValueError as err:
			print ('Invalid value :(')
			sys.exit()
	print (list)

remove_duplicates([1,1,2]) # -> [1,2]
remove_duplicates([0,0,1,1,1,2,2,3,3,4]) # -> [0,1,2,3,4]
remove_duplicates([1,1,1,1,1,1,1,1]) # -> [1]