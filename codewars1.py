# 1
'''Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
Can you help her?'''


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# 2
'''write me a function stringy that takes a size and returns a string of alternating 1s and 0s.
the string should start with a 1.
a string with size 6 should return :'101010'.with size 4 should return : '1010'.
with size 12 should return : '101010101010'.
The size will always be positive and will only use whole numbers.'''


def stringy(size):
    newstring = ''
    for i in range(size):
        if i % 2 != 0:
            newstring += '0'
        else:
            newstring += '1'
    return newstring


# 3
'''Sometimes, I want to quickly be able to convert miles per imperial gallon (mpg) into kilometers per liter (kpl).
Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).
Make sure to round off the result to two decimal points.
Some useful associations relevant to this kata:
1 Imperial Gallon = 4.54609188 litres
1 Mile = 1.609344 kilometres'''


def converter(mpg):
    return round(mpg / (4.54609188 / 1.609344), 2)


# 4
'''Issue
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.
The pipes connecting your level's stages together need to be fixed before you receive any more complaints.
The pipes are correct when each pipe after the first is 1 more than the previous one.
Task
Given a list of unique numbers sorted in ascending order, return a new list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).
Example
Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8'''


def pipe_fix(nums):
    newnums = [nums[0]]
    for i in nums[1:]:
        if i - newnums[-1] == 1:
            newnums.append(i)
        else:
            for j in range (newnums[-1]+1, i+1):
                newnums.append(j)
    return newnums

'''5
Your task is to create a function that does four basic mathematical operations.
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7'''


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '/':
        return value1 / value2
    elif operator == '*':
        return value1 * value2
    return f'Invalid operator {operator}'


'''6
Find the sum of all multiples of n below m
Keep in Mind n and m are natural numbers (positive integers)
m is excluded from the multiples 
Examples
sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID"
'''
def sum_mul(n, m):
    mul=0
    i=1
    if (m<=0 or n<=0):
        return ("INVALID")
    while n*i<m:
        mul+=n*i
        i+=1
    return mul

'''7
Bob needs a fast way to calculate the volume of a cuboid with three values: 
the length, width and height of the cuboid. 
Write a function to help Bob with this calculation.'''
def get_volume_of_cuboid(length, width, height):
    return length*width*height

'''8
Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go. 
Don Drumphet wants to build a wall between his house and his neighbor’s, and is trying to get the neighborhood 
association to pay for it. He begins to solicit his neighbors to petition to get the association to build the wall. 
Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span, 
and can only remember two letters from each of his neighbors’ names. As he collects signatures, 
he insists that his neighbors keep truncating their names until two letters remain, and he can finally read them.

Your code will show Full name of the neighbor and the truncated version of the name as an array. 
If the number of the characters in name is less than or equal to two, 
it will return an array containing only the name as is"'''
def who_is_paying(name):
    if len(name)<=2: return [name]
    return [name,name[:2]]

'''9
In this kata you will create a function that takes in a list and returns a list with the reverse order.'''
def reverse_list(l):
    return l[::-1]

'''10
The Story:
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. 
With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough 
space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

Task Overview:
You have to write a function that accepts three parameters:
cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus excluding the driver.
wait is the number of people waiting to get on to the bus excluding the driver.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

Usage Examples:
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting
def enough(cap, on, wait):
    return max(0, wait - (cap - on))
'''
def enough(cap, on, wait):
    if cap< on+wait: return on+wait-cap
    return 0

'''11
Write a function which converts the input string to uppercase.
'''
def make_upper_case(s):
    return s.upper()

'''12
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.
You receive an array with your peers' test scores. Now calculate the average and compare your score!
Return True if you're better, else False!
Note:
Your points are not included in the array of your class's points. 
For calculating the average point you may add your point to the given array!'''
def better_than_average(class_points, your_points):
    return your_points>(sum(class_points)/len(class_points))

'''13
When provided with a letter, return its position in the alphabet.
Input :: "a"
Ouput :: "Position of alphabet: 1"'''

def position(alphabet):
    return 'Position of alphabet: '+ str(ord(alphabet)-ord('a')+1)

'''14
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.
Note: input will never be an empty string'''
def fake_bin(x):
    bin_line=''
    for i in x:
        if i<'5': bin_line+='0'
        else: bin_line+='1'
    return bin_line

'''15
Write a function to split a string and convert it into an array of words.'''
def string_to_array(s):
    return s.split(' ')


