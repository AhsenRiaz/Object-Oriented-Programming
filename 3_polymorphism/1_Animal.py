# Polymorphism in object-oriented programming (OOP) refers to the ability of different classes or objects to be treated as instances of a common type. It allows for a single interface or method name to be used for objects of various types, and the behavior is determined by the type of the object at runtime. Polymorphism enhances code flexibility, readability, and maintainability.

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Dog(Animal):
    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")

    def show_affection(self):
        print(f"{self.name} wags tail")


class Cat(Animal):
    def swatstring(self):
        print(f"{self.name} shreds the string")

    def show_affection(self):
        print(f"{self.name} purrs")


for a in (Dog("Rover"), Cat('Fluffy')):
    a.show_affection()
