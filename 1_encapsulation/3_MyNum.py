
class MyNum:
    def __init__(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val = self.val + 1


aa = MyNum("hh")
bb = MyNum(100)

aa.increment()
aa.increment()
bb.increment()

print(aa.val)
print(bb.val)
