#multi-level-inheritnance
#A is base class
#B is derived from A
#C is derived from B
class A:
    def show(self):
        print("Class A")
    def printA(self):
        print("printA() inside Class A")

class B(A):
    def show(self):
        print("Class B derived from A")
    def printB(self):
        print("printB() inside Class B")

class C(B):
    def show(self):
        print("Class C derived from B")
    def printC(self):
        print("printC() inside Class C")
#object creation
print("\n--- Example 1 ---")
a=A()
b=B()
c=C()
a.show()
b.show()
b.printA()
b.printB()
c.show()
c.printA()
c.printB()
c.printC()

#2
class Animal:
    def __init__(self, species):
        self.species = species
        
    def show(self):
        print(f"I am an Animal of species: {self.species}")

class Mammal(Animal):
    def __init__(self, species, sound):
        # Calling the parent (Animal) constructor
        super().__init__(species)
        self.sound = sound
        
    def walk(self):
        print(f"The {self.species} is walking.")

class Dog(Mammal):
    def __init__(self, species, sound, breed):
        # Calling the parent (Mammal) constructor
        super().__init__(species, sound)
        self.breed = breed
        
    def bark(self):
        print(f"The {self.breed} dog says {self.sound}!")

print("\n--- Example 2 ---")
# Creating a Dog object automatically chains up to Mammal, and then up to Animal to initialize everything!
my_dog = Dog("Canine", "Woof", "Golden Retriever")

my_dog.show() # Inherited directly from Animal
my_dog.walk() # Inherited directly from Mammal
my_dog.bark() # Defined directly in Dog

#3
class Device:
    def __init__(self, device_type):
        self.device_type = device_type
        
    def display_info(self):
        print(f"Device type: {self.device_type} device")

# Remember to formally inherit! Type(Device)
class Type(Device):
    def __init__(self, device_type, current):
        super().__init__(device_type)
        self.current = current
        
    def display_info(self):
        print(f"Device type: {self.device_type} device, Current: {self.current}")

# Remember to formally inherit! SmartPhone(Type)
# Note: Renamed Gadget to SmartPhone to match the instantiation name later in your code
class SmartPhone(Type):
    def __init__(self, device_type, current, voltage):
        super().__init__(device_type, current) 
        
        # Changed this to 'voltage' because your print statement expects self.voltage
        self.voltage = voltage
         
    def display_info(self):
        print(f"Device type: {self.device_type} device, current: {self.current}, voltage: {self.voltage}")

#object creation
print("\n--- Example 3 ---")
# Device only requires 1 argument (device_type)
device = Device("Generic")

# Type requires 2 arguments (device_type, current)
dev_type = Type("Wired", "AC")

# SmartPhone requires 3 arguments (device_type, current, voltage)
smartphone = SmartPhone("Mobile", "DC", "5 Volts")

device.display_info()
dev_type.display_info()
smartphone.display_info()
