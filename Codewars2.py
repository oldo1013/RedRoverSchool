# return masked string
def maskify(cc):
    masked = ''
    for i in range(len(cc) - 4):
        masked += '#'
    masked += cc[-4:]
    return masked


'''You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones -- 
everytime you press the button it sends you an array of one-letter strings representing directions to walk 
(eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) 
and you know it takes you one minute to traverse one city block, so create a function that will return true 
if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, 
of course, return you to your starting point. Return false otherwise.
'''


def is_valid_walk(walk):
    n, s, w, e = 0, 0, 0, 0
    for i in walk:
        if i == 'n':
            n += 1
        elif i == 'e':
            e += 1
        elif i == 's':
            s += 1
        elif i == 'w':
            w += 1
    return (len(walk) == 10 and (n - s) == 0 and (e - w) == 0)


def find_outlier(integers):
    if (integers[0] % 2 == integers[1] % 2 != 0 or integers[1] % 2 == integers[2] % 2 != 0 or integers[0] % 2 ==
            integers[2] % 2 != 0):
        return [i for i in integers if i % 2 == 0][0]
    else:
        return [i for i in integers if i % 2 != 0][0]


'''Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. 
The box is special because it has the ability to change gravity.
There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. 
At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity, 
it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right). 
Below is an example of what a box of cubes might look like before and after switching gravity.'''
# +---+                                       +---+
# |   |                                       |   |
# +---+                                       +---+
# +---++---+     +---+              +---++---++---+
# |   ||   |     |   |   -->        |   ||   ||   |
# +---++---+     +---+              +---++---++---+
# +---++---++---++---+         +---++---++---++---+
# |   ||   ||   ||   |         |   ||   ||   ||   |
# +---++---++---++---+         +---++---++---++---+
'''Given the initial configuration of the cubes in the box, 
find out how many cubes are in each of the n columns after Bob switches the gravity.'''


def flip(d, a: list):
    if d == 'R':
        a.sort()
    else:
        a.sort(reverse=True)
    return a


def cookie(x):
    if type(x) is str:
        name = "Zach"
    elif type(x) in (float, int):
        name = "Monica"
    else:
        name = 'the dog'
    return f'Who ate the last cookie? It was {name}!'


def smash(words: list):
    return " ".join(str(x) for x in words)


def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

'''I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated: 
The number I'm afraid of depends on which day of the week it is... 
This is a concrete description of my mental illness:
Monday --> 12
Tuesday --> numbers greater than 95
Wednesday --> 34
Thursday --> 0
Friday --> numbers divisible by 2
Saturday --> 56
Sunday --> 666 or -666
Write a function which takes a string (day of the week) and an integer (number to be tested) so it tells the doctor 
if I'm afraid or not. (return a boolean)'''
def am_I_afraid(day,num):
    if ((day=='Monday' and num==12) or (day=='Tuesday' and num>95) or
            (day=='Wednesday' and num==34) or (day=='Thursday' and num>0) or
            (day=='Friday' and num%2==0) or (day=='Saturday' and num==56) or (day=='Sunday' and num in (666,-666))): return True
    else: return False

'''Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds easy enough, 
right? Well, let's see if you can do it!
You will have to define a function, which will be given an hour (always in the range of 1 to 12, inclusive), 
a minute (always in the range of 0 to 59, inclusive), and a period (either a.m. or p.m.) as input.
Your task is to return a four-digit string that encodes that time in 24-hour time.
Notes:
By convention, noon is 12:00 pm, and midnight is 12:00 am.
On 12-hours clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On 24-hour clock, this translates to 0015.'''
def to24hourtime(hour, minute, period):
    hour,minute=str(hour).zfill(2), str(minute).zfill(2)
    if period == 'am':
        if hour !=12:  return hour+minute
        else: return '00'+minute
    else:
        if hour !=12:  return str(int(hour)+12)+minute
        else: return '12'+minute


def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split(' '))

def drop_cap(words):
    return " ".join(word.capitalize() if len(word) > 2 else word for word in words.split(' '))

'''Write a function that takes as parameters an array (arr) and 2 integers (x and y). 
The function should return the mean between the mean of the the first x elements of the array and the mean of the 
last y elements of the array.
The mean should be computed if both x and y have values higher than 1 but less or equal to the array's length. 
Otherwise the function should return -1.
Examples
[1, 3, 2, 4], 2, 3 => should return 2.5
because: the mean of the the first 2 elements of the array is (1+3)/2=2 and the mean of the last 3 elements of the array is (4+2+3)/3=3 so the mean of those 2 means is (2+3)/2=2.5.
[1, 3, 2, 4], 1, 2 => should return -1
because x is not higher than 1.
[1, 3, 2, 4], 2, 8 => should return -1
because 8 is higher than the array's length.'''
def get_mean(arr,x,y):
    if x<=1 or y<=1 or x>len(arr) or y>len(arr):
        return -1
    else:
        return ((sum(arr[:x])/len(arr[:x]))+(sum(arr[-y:])/len(arr[-y:])))/2


'''Filter the number
Oh, no! The number has been mixed up with the text. 
Your goal is to retrieve the number from the text, can you return the number back to its original state?
Task
Your task is to return a number from a string.
Details
You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string in 
the order they occur.'''
def filter_string(st):
    numbers=''
    for i in st:
        if i.isdigit():
            numbers+=i
    return numbers

def filter_string_better(string):
    return int(''.join(filter(str.isdigit, string)))


def spacey(array):
    new_array=[array[0]]
    for i in array[1:]:
        new_array.append(new_array[-1]+i)
    return new_array

'''Given two positive integers m (width) and n (height), fill a two-dimensional list (or array) of size 
m-by-n in the following way:
(1) All the elements in the first and last row and column are 1.
(2) All the elements in the second and second-last row and column are 2, excluding the elements from step 1.
(3) All the elements in the third and third-last row and column are 3, excluding the elements from the previous steps.

And so on ...'''

def make_grid(total_rows, total_columns):
    grid=[]
    for row in range(total_rows):
        line=[]
        for column in range(total_columns):
            line.append(min(row + 1, total_rows - row, column + 1, total_columns - column))
        grid.append(line)
    return grid


import math;
def check_logs(log):
    res = 0
    stamp = []
    if len(log)==1: return 1
    for i in log:
        hour,minutes,seconds=i.split(":")
        stamp.append(int(hour)*3600+int(minutes)*60+int(seconds))
    for s in range(len(stamp)-1):
        print(stamp)
        if stamp[s+1]-stamp[s]<=0: stamp[s+1]+=86400
        print(res)
        res+=stamp[s]
        print(str(res)+' after')
    res+=stamp[-1]
    return math.ceil(((res/86400))) if log[0]!='00:00:00' else math.ceil(((res-86400)/86400))






def get_count(sentence):
    return sum(1 for i in sentence if i in ('a', 'e', 'i', 'o', 'u'))


def greet_jedi( first:str, last: str):
    return ''.join((last.capitalize()[:3]+ first.capitalize()[:2]))


'''Definition
A Tidy number is a number whose digits are in non-decreasing order.
Task
Given a number, Find if it is Tidy or not .
'''
def tidyNumber(n):
    arr=[]
    for i in str(n):arr.append(i)
    arr2=sorted(arr)
    return arr==arr2

'''You will be given an array that contains two strings. 
Your job is to create a function that will take those two strings and transpose them, 
so that the strings go from top to bottom instead of left to right.'''
#solution via zip

def transpose_two_strings(arr):
    result = ''
    st_1=[' ']* max(len(arr[0]),len(arr[1]))
    st_2=[' ']* max(len(arr[0]),len(arr[1]))
    for i in range(len(arr[0])):
        st_1[i]=arr[0][i]
    for j in range(len(arr[1])):
        st_2[j]=arr[1][j]
    for i in range(len(st_1)-1):
        result+=st_1[i]+ ' '+ st_2[i] +'\n'
    result+=st_1[-1]+ ' '+ st_2[-1]
    return result





