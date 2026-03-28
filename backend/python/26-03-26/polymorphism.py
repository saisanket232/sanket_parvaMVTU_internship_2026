#Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). In Python, polymorphism is achieved through method overriding and duck typing.
# a single interface to represent different underlying forms (data types). In Python, polymorphism is achieved through method overriding and duck typing.
#Poly+morphism allows us to write code that can work with objects of different types, as long as they implement the same interface. This promotes code reusability and flexibility.

#types of polymorphism in python:
# 1. Compile-time polymorphism (Method Overloading)
# 2. Run-time polymorphism (Method Overriding)
# 3.duck typing
#4 .operator overloading
#5 .Polymorphic functions and Classes

#Built in polymorphic functions

name="Retro"
hobbies=["Coding", "Gaming", "Traveling"]
skills={"Python": "Advanced", "Java": "Intermediate", "C++": "Beginner"}
print("Length of name:", len(name)) #5
print("Length of hobbies:", len(hobbies)) #3
print("Length of skills:", len(skills)) #3

# type()
print("Type of name:", type(name)) #<class 'str'>
print("Type of hobbies:", type(hobbies)) #<class 'list'>
print("Type of skills:", type(skills)) #<class 'dict'>

#sum()
print("Sum of list [1, 2, 3]:", sum([1, 2, 3])) #6
print("Sum of tuple (4, 5, 6):", sum((4, 5, 6))) #15

#custom methods with polymorphism
def display(value):
    print(f"Value: {value}, Type: {type(value)}")

display("Retro") #Value: Retro, Type: <class 'str'>
display(42) #Value: 42, Type: <class 'int'> 
display([1, 2, 3]) #Value: [1, 2, 3], Type: <class 'list'>
display(59590.99) #Value: 59590.99, Type: <class 'float'>

def findarea(side, side1, side2=None, side3=None):
    print("Area of a shape cannot be determined without specific dimensions.")
    if side==1:
        print(f"Area of Square with side {side1} is: {side1*side1}")
    elif side==2:
        print(f"Area of Rectangle with length {side1} and breadth {side2} is: {side1*side2}")
    elif side==3:
        print(f"Area of Triangle with base {side1} and height {side2} is: {(side1*side2*side3)/3}")

findarea(1, 5) #Area of Square with side 5 is: 25
findarea(2, 5, 10) #Area of Rectangle with length 5 and breadth 10 is: 50
findarea(3, 5, 10, 2) #Area of Triangle with base 5 and height 10 is: 100