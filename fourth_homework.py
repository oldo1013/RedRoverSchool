'''4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения
(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35
	position: web developer

4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
     положительные числа

4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке (my_list)
4.5. Напишите декоратор, который высчитывает время работы функции, которую он принимает в качестве параметра
4.6. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
     Примените эти функции в качестве методов в другом файле.
'''
#Task 4.1
from math import sqrt
def square(side):
    return (side*4,side*side,side*sqrt(2))

# Task 4.2

def printing(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')

# Task 4.3
my_list = [20, -3, 15, 2, -1, -21]
positive_my_list = list(filter(lambda num: num > 0, my_list))

# Task 4.4
from functools import reduce
my_list = [20, -3, 15, 2, -1, -21]
p = reduce((lambda x, y: x * y), my_list)

# Task 4.5
import time
def execution_time(func):
    def wrapper(**kwargs):
        start_time=time.perf_counter()
        print(f'Start time: {start_time}')
        func(**kwargs)
        end_time=time.perf_counter()
        print(f'End time: {end_time}')
        print(f'Elapced_time={end_time-start_time}')
    return wrapper
@execution_time
def printing_wrapped(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')

printing_wrapped(last_name='Popov', name='Max', age=40, position='web developer')

# Task 4.6
from my_calc import *

summarization=summa(4,5)
print(summarization)
minusation= raznost(9,6)
print(minusation)
multiplication=multiply(2,3)
print(multiplication)
divading=divade(6,2)
print(divading)
divading_to_zero=divade(3,0)
print(divading_to_zero)