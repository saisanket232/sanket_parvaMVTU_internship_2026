#hierarchical-inheritance
#A Base class and B and C are derived from A

class A:
    def print(self):
        print("Class A is a Base Class")
class B(A):
    def print(self):
        print("Class B is derived from A")
class C(A):
    def print(self):
        print("Class C is derived from A")
class D(A):
    def print(self):
        print("Class D is derived from A")
#object creation
print("\n--- Example 1 ---")
a=A()
b=B()
c=C()
d=D()
a.print()
b.print()
c.print()
d.print()

#2
class Animal:
    def animal(self):
        print("Animal class method")
class Dog(Animal):
    def dog(self):
        super().animal()
        print("Dog class method")
class Cat(Animal):
    def cat(self):
        super().animal()
        print("Cat class method")
class Bird(Animal):
    def bird(self):
        print("Bird class method")
#object creation
print("\n--- Example 2 ---")
animal=Animal()
dog=Dog()
cat=Cat()
bird=Bird()
animal.animal()
dog.animal()
dog.dog()
cat.animal()
cat.cat()
bird.animal()
bird.bird()

#3
class Vehicle:
    def __init__(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels
    def vehicle(self):
        print("Vehicle class method")
class Car(Vehicle):
    def car(self):
        super().vehicle()
        print("Car class method")
class Bike(Vehicle):
    def bike(self):
        super().vehicle()
        print("Bike class method")
class Truck(Vehicle):
    def truck(self):
        super().vehicle()
        print("Truck class method")
#object creation
print("\n--- Example 3 ---")
vehicle=Vehicle()
car=Car()
bike=Bike()
truck=Truck()
vehicle.vehicle()
car.vehicle()
car.car()
bike.vehicle()
bike.bike()
truck.vehicle()
truck.truck()
