
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

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(10)
b = InstanceCounter(20)
c = InstanceCounter(30)

for obj in (a, b, c):
    print("val of obj: ", obj.get_val())
    print("count : ", obj.get_count())
