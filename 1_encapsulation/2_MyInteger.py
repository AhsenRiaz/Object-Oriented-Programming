
class MyInteger:
    def set_val(self, val):
        try:
            self.val = int(val)
        except ValueError:
            return
        self.val = val

    def get_value(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1


i = MyInteger()
i.set_val(9)
print(i.get_value())
print(i.increment_val())
print(i.get_value())
