#single inheritance
#"Base class" Derives a "Derived class" 
#"Derived class" inherits the properties of "Base class"
#base class
class A:
    def show(self):
        print("Base class")
#derived class
class B(A):
    def show(self):
        print("Derived class")
#object creation
print("\n--- Example 1 ---")
a=A()
b=B()
a.show()
b.show()

#2
class Vehicle:
    def showVehicleInfo(self):
        print("Vehicle Started !")
class Car(Vehicle):
    def showCarInfo(self):
        print("Car Started !")
#object creation
print("\n--- Example 2 ---")
car=Car()
car.showVehicleInfo()
car.showCarInfo()

#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def displayPersonInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # Calling the parent class (Person) constructor using super()
        super().__init__(name, age)
        self.student_id = student_id
        
    def displayStudentInfo(self):
        print(f"Student ID: {self.student_id}")

# Object creation for Example 3
print("\n--- Example 3 ---")
student = Student("Sanket", 22, "STU1001")
# Accessing base class method
student.displayPersonInfo()  
# Accessing derived class method
student.displayStudentInfo() 

#4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def work(self):
        print(f"{self.name} is doing regular employee work.")

# Derived class inheriting from Employee
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Using super() to call parent constructor
        super().__init__(name, salary)
        self.department = department
        
    def work(self):
        # Using super() to invoke the parent class's overridden method!
        super().work()
        print(f"{self.name} is also managing the {self.department} department.")

print("\n--- Example 4 ---")
manager = Manager("Alice", 85000, "IT")
# When we call work(), it will trigger the Manager's work(), which uses super() to also trigger Employee's work()
manager.work()
