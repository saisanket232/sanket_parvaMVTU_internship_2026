#multiple-Inheritance
#it is a type of inheritance in which a class can inherit from more than one class
#syntax: class Child(Parent1, Parent2, Parent3, ...):


#Example 1
class A:
    def displayA(self):
        print("Class A is a base Class")
class B:
    def displayB(self):
        print("Class B is a base Class")
class C(A,B):
    def displayC(self):
        print("Class C is a derived Class")
#object creation
print("\n--- Example 1 ---")
a=A()
b=B()
c=C()
a.displayA()
b.displayB()
c.displayA()
c.displayB()
c.displayC()

#2
class father:
    def father(self):
        print("Father class method")
class mother:
    def mother(self):
        print("Mother class method")
class child(father,mother):
    def child(self):
        print("Child class method")
#object creation
print("\n--- Example 2 ---")
child=child()
child.father()
child.mother()
child.child()

#3
class Camera :
    def camera(self):
        print("Camera class method")
class Wifi:
    def wifi(self):
        print("Wifi class method")
class Bluetooth:
    def bluetooth(self):
        print("Bluetooth class method")
class Smartphone(Camera,Wifi,Bluetooth):
    def smartphone(self):
        print("Smartphone class method")
#object creation
print("\n--- Example 3 ---")
smartphone=Smartphone()
smartphone.camera()
smartphone.wifi()
smartphone.bluetooth()
smartphone.smartphone()