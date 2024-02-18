'''3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

3.2 Дан список list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'

3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж

3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение

3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]

3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга
     '''

# Task 3.1
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])

# Task 3.2
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
s = 0
for i in list_1:
    if isinstance(i, int):
        s += i
    elif "a" in i:
        print(i)
print(s)

# Task 3.3
print(tuple(['cat', 'dog', 'horse', 'cow']))

# Task 3.4
family1 = tuple(input('Введите текст через запятую: ').split(','))
family2 = tuple(input('Введите текст через запятую: ').split(','))
if len(family1) == len(family2):
    print('Equal')
elif len(family1) > len(family2):
    print('family1')
else:
    print('family2')

# Task 3.5
film = {'title': 'Avatar', 'director': 'James Cameron', 'year': 2009,
        'budget': '237 million', 'main_actor': 'Sam Worthington',
        'slogan': 'Their world. A new home. Discover a new world.'}
print(film.keys())
print(film.values())
print(film.items())

# Task 3.6
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
result=0
for i in my_dictionary.values():
    result+=i
print(result)

# Task 3.7
first_list=[1, 2, 3, 4, 5, 3, 2, 1]
result_list=set(first_list)
print(result_list)

# Task 3.8

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

print(set1.intersection(set2))
print(set2.symmetric_difference(set1))
print(set1.issubset(set2))
print(set2.issubset(set1))

