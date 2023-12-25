# a decorator is a special type of function that can be used to modify the behavior of another function or method.

# A decorator is applied to a function or method using the @decorator syntax just above its definition. Decorators are themselves functions that take another function as an argument and return a new function.

# a static method is associated with the class rather than instances. It cannot access or modify instance-specific data and is primarily used for functionality that is related to the class but does not depend on the state of individual instances.

class InstanceCounter:
    # class attributes are shared among all instances.
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(10)
b = InstanceCounter(20)
c = InstanceCounter("hello")

print(a.filterint(10))
