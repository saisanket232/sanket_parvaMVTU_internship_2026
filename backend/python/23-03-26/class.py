# Basic syntax of a class in Python
# class ClassName:
    # attributes (variables that store data)
    # methods (functions that perform actions)

# Defining a class named 'Student'
class Student:

    # constructor method
    # '__init__' is a special method automatically called when a new object is created to initialize its attributes
    def __init__(self, name, age, clg, branch, sem):
        self.name = name      # Assigning the passed 'name' to the object's 'name' attribute
        self.age = age        # Assigning the passed 'age' to the object's 'age' attribute
        self.clg = clg        # Assigning the passed 'clg' to the object's 'clg' attribute
        self.branch = branch  # Assigning the passed 'branch' to the object's 'branch' attribute
        self.sem = sem        # Assigning the passed 'sem' to the object's 'sem' attribute
        
    # An instance method
    def printDetails(self):
        # Prints a simple message along with the student's name
        print("Student Details !!!", self.name)

# Redefining the 'Student' class (Note: This completely overwrites the first class definition above)
class Student:

    # parameterized constructor with a default value for 'clg'
    # If no college is provided during object creation, it defaults to "ParvaM Tech"
    def __init__(self, name, age, branch, sem, clg="ParvaM Tech"):
        self.name = name      # Assigning the 'name' parameter to the instance variable
        self.age = age        # Assigning the 'age' parameter to the instance variable
        self.branch = branch  # Assigning the 'branch' parameter to the instance variable
        self.sem = sem        # Assigning the 'sem' parameter to the instance variable
        self.clg = clg        # Assigning the 'clg' parameter to the instance variable

    # Method to print all the details of the student
    def printDetails(self):
        # Prints a header message
        print("Student Details !!!")
        # Uses an f-string to format and print all attributes nicely on a single line
        print(f"Name of the student : {self.name} , Age of the student : {self.age} , College of the student : {self.clg} , Branch of the student : {self.branch} , Semester of the student : {self.sem}")


# Creating the first Student object 'std1' and passing all 5 arguments
# It overwrites the default college value with '8' (looks like an integer was passed by mistake for college)
std1 = Student("Retro", 20, "AIT", "AI", 8)
# Calling the printDetails method on the 'std1' object to display its data
std1.printDetails()   

# Printing a new line character for better spacing in the terminal output
print("\n")

# Creating the second Student object 'std2' and passing all 5 arguments
std2 = Student("Sai", 24, "IIT", "ic", 10)
# Calling the printDetails method on the 'std2' object
std2.printDetails()

# Printing another new line character
print("\n")

# Creating the third Student object 'std3' and passing only 4 arguments
# Because the 5th argument ('clg') is missing, it will use the default value "ParvaM Tech"
std3 = Student("Sanket", 26, "AIhhh", 3)
# Calling the printDetails method for 'std3'
std3.printDetails()

# General syntax for Object Creation and Method Calling:
# objectName = ClassName(arguments)
# objectName.methodName()
