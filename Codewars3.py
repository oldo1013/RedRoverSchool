'''Color Ghost
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
'''
import math
import random


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost = Ghost()

'''Write a class Block that creates a block (Duh..)
Requirements
The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.

Define these methods:
`get_width()` return the width of the `Block`
`get_length()` return the length of the `Block`
`get_height()` return the height of the `Block`
`get_volume()` return the volume of the `Block`
`get_surface_area()` return the surface area of the `Block`
Note: no error checking is needed'''


class Block:
    def __init__(self, array):
        self.width = array[0]
        self.length = array[1]
        self.height = array[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return (self.height * self.length * self.width)

    def get_surface_area(self):
        return ((2 * self.height * self.length) + (2 * self.length * self.width) + (2 * self.height * self.width))


block1 = Block([2, 2, 2])

'''Now that we have a Block let's move on to something slightly more complex: a Sphere.
Arguments for the constructor
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)
Methods to be defined
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
'''


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return (round((4 / 3 * math.pi * (self.radius ** 3)), 5))

    def get_surface_area(self):
        return (round((4 * math.pi * (self.radius ** 2)), 5))

    def get_density(self):
        return (round((self.mass / self.get_volume()), 5))


ball = Sphere(2, 50)

'''This kata is about static method that should return different values.
On the first call it must be 1, on the second and others - it must be a double from previous value.'''


class Class:
    value = 1

    @staticmethod
    def get_number():
        result = Class.value
        Class.value *= 2
        return result


'''You are a leader of a small pirate crew. And you have a plan.
With the help of OOP you wish to make a pretty efficient system to identify ships with heavy booty on board!
Unfortunately for you, people weigh a lot these days, so how do you know if a ship is full of gold and not people?
You begin with writing a generic Ship class / struct:
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
Every time your spies see a new ship enter the dock, they will create a new ship object based on their observations:
draft - an estimate of the ship's weight based on how low it is in the water
crew - the count of crew on board
Titanic = Ship(15, 10)
Task
You have access to  "draft" and "crew". "Draft" is the total ship weight and "crew" is the number of humans on the ship.
Each crew member adds 1.5 units to the ship draft. If after removing the weight of the crew, the draft is still more
than 20, then the ship is worth looting. Any ship weighing that much must have a lot of booty!
Add the method
is_worth_it
to decide if the ship is worthy to loot. For example:
Titanic.is_worth_it()
False
Good luck and may you find GOOOLD!'''


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    # Your code here
    def is_worth_it(self):
        return (self.draft - (self.crew * 1.5)) > 20


'''Background
You're modelling the interaction between a large number of quarks and have decided to create a Quark class so you
can generate your own quark objects.
Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.
Your task
Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green") and any valid
flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').
Every quark has the same baryon_number (BaryonNumber in C#): 1/3.
Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact with another
quark via the strong force. When two quarks interact they exchange colors.'''


class Quark(object):
    baryon_number = 1 / 3

    def __init__(self, color, flavour):
        self.color = color
        self.flavour = flavour

    def interact(self, object):
        col = self.color
        self.color = object.color
        object.color = col
        return self.color


'''At the end of the last semester, Prof. Joey Greenhorn implemented an online report card for his students in order
to save paper. Everything seemed to be working fine back then, but since the start of the new semester he has
received several emails from students complaining about erroneous grades showing up in their online report cards.
Can you help him correct his implementation of the "Student" class?'''


class Student:
    def __init__(self, first_name, last_name, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def add_grade(self, grade):
        if self.grades is None:
            self.grades = []
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)


'''You are the judge at a competitive eating competition and you need to choose a winner!
There are three foods at the competition and each type of food is worth a different amount of points.
Points are as follows:
Chickenwings: 5 points
Hamburgers: 3 points
Hotdogs: 2 points
Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the
participants, for example:
[  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}]
It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.
[  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}]
Happy judging!'''


class Participant:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"{{'name': '{self.name}', 'score': {self.score}}}"

    def __repr__(self):
        return self.__str__()

    def add_score(self, item, quantity):
        if item == 'chickenwings':
            self.score += quantity * 5
        elif item == 'hamburgers':
            self.score += quantity * 3
        elif item == 'hotdogs':
            self.score += quantity * 2


def scoreboard(who_ate_what):
    unsorted = []
    for i in who_ate_what:
        person = Participant(' ')
        for key, value in i.items():
            if key == 'name':
                person.name = value
            else:
                person.add_score(key, value)
        unsorted.append(person)
    sorted_board = map(lambda x: {"name": x.name, "score": x.score}, sorted(unsorted, key=lambda x: (-x.score, x.name)))
    return list(sorted_board)


# print(scoreboard([{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},
#                                        {"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},
#                                       {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
#                                       {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]))
# [{"name": "Big Bob", "score": 134},{"name": "Billy The Beast", "score": 122},
#  {"name": "Habanero Hillary", "score": 98},{"name": "Joey Jaws", "score": 94}])
'''Timmy's quiet and calm work has been suddenly stopped by his project manager (let's call him boss) yelling:
- Who named these classes?! Class MyClass? It's ridiculous! I want you to change it to UsefulClass!
Tim sighed, he already knew it's gonna be a long day.
Few hours later, boss came again:
Much better - he said - but now I want to change that class name to SecondUsefulClass,and went off.
Although Timmy had no idea why changing name is so important for his boss, he realized, that it's not the end,
so he turned to you, his guru, to help him and asked you to prepare some function,
which could change name of given class.
Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
but starting only with upper case letter. In other case it should raise an exception.
Disclaimer: there are obviously betters way to check class name than in example cases, but let's stick with that,
that Timmy yet has to learn them.
'''


class MyClass:
    pass


myObject = MyClass();
new_name = 'test'
import re


def class_name_changer(cls, new_name):
    if new_name[0] != new_name[0].upper():
        raise Exception("New name should be capitalized!")
    elif (re.fullmatch(r'^[a-zA-z]\w*', new_name)) == None:
        raise Exception("Proposed function should allow only names with alphanumeric chars!")
    else:
        cls.__name__ = new_name
    return cls.__name__


# better version
def class_name_changer_alnum(cls, new_name):
    assert new_name[0].isupper() and new_name.isalnum()
    cls.__name__ = new_name


'''The following code was thought to be working properly, however when the code tries to access the age of the person
instance it fails.
person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name)
print(person.age)
For this exercise you need to fix the code so that it works correctly.
Note: the order of the person's full name is first name and last name.'''


class Person():

    def __init__(self, first_name, last_name, age):
        self.full_name = f'{first_name} {last_name}'
        self.age = age


person = Person('Yukihiro', 'Matsumoto', 47)

'''Write a function, factory, that takes a number as its parameter and returns another function.
The returned function should take an array of numbers as its parameter,
and return an array of those numbers multiplied by the number that was passed into the first function.
In the example below, 5 is the number passed into the first function.
So it returns a function that takes an array and multiplies all elements in it by five.'''


def factory(x):
    def multipl(a):
        return [i * x for i in a]

    return multipl


# fives = factory(5)          # returns a function - fives
# my_array = [1, 2, 3]
# print(fives(my_array))

'''Description
Lets imagine a yoga classroom as a Square 2D Array of Integers classroom, with each integer representing a person,
and the value representing their skill level.
classroom = [
            [3,2,1,3],
            [1,3,2,1],
            [1,1,1,2],
            ]
poses = [1,7,5,9,10,21,4,3]
During a yoga class the instructor gives a list of integers poses representing a yoga pose that each person
in the class will attempt to complete.
A person can complete a yoga pose if the sum of their row and their skill level is greater than or equal to the
value of the pose.
Task
Your task is to return the total amount poses completed for the entire classroom.
Example
classroom = [
            [1,1,0,1], #sum = 3
            [2,0,6,0], #sum = 8
            [0,2,2,0], #sum = 4
            ]

poses = [4, 0, 20, 10]
3 people in row 1 can complete the first pose
Everybody in row 1 can complete the second pose
Nobody in row 1 can complete the third pose
Nobody in row 1 can complete the fourth pose
The total poses completed for row 1 is 7
You'll need to return the total for all rows and all poses.
Translations are welcomed!'''


def yoga(classroom, poses):
    amount = 0
    if len(classroom) == 0 or len(poses) == 0:
        return 0
    for row in classroom:
        summa = sum(row)
        for pose in poses:
            for per in row:
                if (per + summa) >= pose:
                    amount += 1
    return amount


# classroom = [
#         [2, 1],  # sum = 3
#         [0,0]  # sum = 8
#         ]  # sum = 4
# poses = [4, 0, 20, 10]
#
# print(yoga(classroom,poses))

'''Create a class that imitates a select screen. The cursor can move to left or right!
In the display method, return a string representation of the list, 
but with square brackets around the currently selected element. 
Also, create the methods to_the_right and to_the_left which moves the cursor.
The cursor should start at index 0.'''

class Menu:
    def __init__(self,list):
        self.list=list
        self.index = 0

    def to_the_right(self):
        if (self.index+1)>len(self.list)-1:
            self.index=0
        else:
            self.index += 1
    def to_the_left(self):
        if (self.index-1)<0:
            self.index=len(self.list)-1
        else:
            self.index -= 1

    def display(self):
        res = list(map(lambda x: f"'{str(x)}'", self.list))
        res[self.index] = f"[{res[self.index]}]"

        return f"[{','.join(res)}]"

'''Create a function that will make anything true'''
def anything(thing):
    class AlwaysTrue:
        def __eq__(self,thing):
            return True
        def __ne__(self,thing):
            return True
        def __gt__(self,thing):
            return True
        def __ge__(self,thing):
            return True
        def __lt__(self,thing):
            return True
        def __le__(self,thing):
            return True

    return AlwaysTrue()

'''I don't like writing classes like this:
class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color
Give me the power to create a similar class like this:
Animal = make_class("name", "species", "age", "health", "weight", "color")
'''
def make_class(*attr_names):
    class Class:
        def __init__(self,*args):
            for name, value in zip(attr_names, args):
                setattr(self, name, value)
    return Class

'''Timmy was thinking about it for while than decided to contact with his guru - you - and ask about it. You offered him to build class that could be inherited, and could provide some class method to modify name of already existing classes. The new class should be named as
ReNameAbleClass
and the special one method should be
change_class_name
Like before, be sure that new solution will allow only names with alphanumeric chars (upper & lower letters plus digits), but starting only with upper case letter.
Moreover, for testing purposes, he want new class to have
__str__
method which will be returning string like "Class name is: MyClass" for MyClass.'''
class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        assert new_name[0].isupper() and new_name.isalnum()
        cls.__name__ = new_name

    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"




