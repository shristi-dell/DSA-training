# Polymorphism
# Polymorphism is an OOP concept where the same method or function performs different actions for different objects or classes.

# Types
# Compile-time Polymorphism (Method Overloading)
# Run-time Polymorphism (Method Overriding)

# Java supports both method overloading and method overriding.
# Python mainly supports method overriding and duck typing.

# def add(a):
#     print(a)
# def add(a,b):
#     print(a+b)
# def add(a,b,c):
#     print(a+b+c)

# #add(11)
# #add(22,33)
# add(11,22,33)



# #overriding
# Method overloading is a feature where multiple methods have
# the same name but different parameters in the same class.

class parent:
    def __init__(self):
        self.speed=100
        print("cash, gold")
    def bike(self):
        print("splender+ ",self.speed)

class child(parent):
     def __init__(self):
        self.speed=150
     def bike(self):
        print("HB ",self.speed)

obj=child()
obj.bike()
 
                      

# Method overriding is a feature where a child class provides a new
#  implementation of a method already defined in the parent class.