class Joe:
    # self is the instance from which the method is called
    def callme(self):
        print("calling 'callMe' method from an instance")
        print(self)


thisjoe = Joe()

# instance is passed to method as the 1st parameter majorly known as "self"
thisjoe.callme()  # <- an instance method

print(thisjoe)
