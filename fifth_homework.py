'''5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
- как минимум один атрибут должен быть с уровнем доступа private.
Соответственно, для получания значений этого атрибута нужно использовать методы get и set.
5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий'''

class Animal:
    def __init__(self, breed, color, price):
        self.breed=breed
        self.color=color
        self.__price=price
    def get_price(self):
        return self.__price

class Dog(Animal):
    def bark(self):
        return f'{self.breed} do bark!'


dog_1= Dog('Corgi','Golden','£2000')
print(dog_1.bark())
print (dog_1.get_price())
