# A class is a blueprint for an instance -> an Instance Factory
class MyClass:
    var = 10

# An instance is an object create from a blueprint
this_obj = MyClass()
that_obj = MyClass()

print(this_obj.var)
print(that_obj.var)
