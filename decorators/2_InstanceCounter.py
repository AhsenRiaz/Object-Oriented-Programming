# class_method is a class method because it is decorated with @classmethod.It takes the cls parameter, referring to the class itself. Class methods can access and operate on class-level data, such as cls.class_variable.

class InstanceCounter:
    # class attributes are shared among all instances.
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(10)
b = InstanceCounter(20)
c = InstanceCounter(30)

for obj in (a, b, c):
    print("val of obj: ", obj.get_val())
    print("count : ", obj.get_count())
