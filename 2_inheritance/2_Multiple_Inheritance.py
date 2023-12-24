# MRO(Method Resolution Order determines the order in which a method is searched in class hierarchy)
# Depth-First approach for searching method

# MRO -> D,B,A,C

class A:
    def do_this(self):
        print("Doing this in A")


class B(A):
    pass


class C:
    def do_this(self):
        print("Doing this in C")


class D(B, C):
    pass


d_instance = D()

d_instance.do_this()

D.mro()
