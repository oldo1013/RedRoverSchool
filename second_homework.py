'''Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре.
Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”

Задание 2.3
Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью input()

Задание 2.5.
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
'''
# #Task 2.1
# health = int(input("Input character health: "))
# if health <= 0:
#     print('False')
# else:
#     print("True")

# #Task 2.2
# number= int(input("Input number: "))
# if (((number%2)==0) and (number!=0)):
#     print("Четное")
# else: print("Нечетное")

##Task 2.3
# year= int(input("Input year: "))
# if ((year%400==0) or ((year%4==0) and (year%100!=0))):
#     print("Високосный")
# else: print("Не Високосный")

##Task 2.4
# text= input('Enter text: ')
# number= int(input('Enter number of lines: '))
# for i in range (number):
#     print(text)

#Task 2.5
num1,num2=int(input("Введите число 1: ")),int(input("Введите число 2: "))
operator= input("Введите один из следющих операторов: +,-, /, * ")
if (operator == '/' and num2==0):
    result= 'На ноль делить нальзя!'
elif operator == '+':
    result= num1+num2
elif operator =='-':
    result= num1 -num2
elif (operator == '/' and num2!=0):
    result= num1/num2
elif operator =='*':
    result= num1*num2
print(f'{num1} {operator} {num2} = {result}')