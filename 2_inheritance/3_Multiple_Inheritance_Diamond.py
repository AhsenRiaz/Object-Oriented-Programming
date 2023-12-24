# In a Diamond Pattern Hierarchy depth-first is used but a bit different
# MRO start search from B and insted of searching in A it goes to class C as A is common and searches in C

# MRO -> D,B,C,A

class A:
    def do_this(self):
        print("Doing this in A")


class B(A):
    pass


class C(A):
    def do_this(self):
        print("Doing this in C")


class D(B, C):
    pass


d_instance = D()

d_instance.do_this()

D.mro()
