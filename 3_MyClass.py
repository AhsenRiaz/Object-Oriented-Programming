import random


class MyClass:
    def dothis(self):
        # self.rand_val is an instance attribute,
        # which is accessible after 'dothis' is called from an instance
        self.rand_val = random.randint(1, 10)


myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)
