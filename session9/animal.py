
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def say_something(self):
        pass

class Cat(Animal):

    def say_something(self):
        print("mew")

class Dog(Animal):

    def say_something(self):
        print("wag")


cat = Cat("fifi")
print(cat.get_name())
cat.say_something()
