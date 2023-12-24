import random


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"The name is {name}")


class Dog(Animal):
    def __init__(self, name):
        # super relates a class to its parent class
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Zu', 'Beagle', 'Mutt'])


def fetch(self, thing):
    print(f"{self.name} goes after the {thing}")


d = Dog("Rover")

print(d.name)
print(d.breed)

f = Dog("Pit")

print(f.name)
print(f.breed)
