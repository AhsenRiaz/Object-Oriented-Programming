# abstraction allows you to hide the implementation details of a class and expose only the necessary functionalities or characteristics

# In Python we can use 'abc' module to create an Abstract Class which can act as a blueprint for sub-classes. In can describe an interface to which methods must be implemented in sub-classes.

from abc import ABC, abstractmethod


# An Abstract Class
class GetterSetter:
    @abstractmethod
    def set_val(self, input):  # a signature with implementation somewhere else
        return

    @abstractmethod
    def get_val(self):
        return


# Inheriting Abstract Class
class MyClass(GetterSetter):
    def set_val(self, input):
        self.val = input

    def get_val(self):
        return self.val


x = MyClass()

x.set_val(10)
print(x.get_val())
