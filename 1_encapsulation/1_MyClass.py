# Encapsulation involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit known as a Class.

# Advantages - Data Hiding, Modularity, Controlled Access, Security, Code Organization

class MyClass:
    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value


a = MyClass()
b = MyClass()

a.set_value(10)
b.set_value(100)

print(a.get_value())
print(b.get_value())
