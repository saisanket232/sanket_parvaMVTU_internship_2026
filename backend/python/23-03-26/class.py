#syntax

#class ClassName:
    #attributes
    #methods

class Student:

    #constructor
    #special method used to initialize the object
    def __init__(self,name,age,clg,branch,sem):
        self.name=name
        self.age=age
        self.clg=clg
        self.branch=branch
        self.sem=sem
    #method
    def printDetails(self):
        print("Student Details !!!",self.name)

class Student:

#parameterized constructor- default values
    def __init__(self, name, age, branch, sem ,clg="ParvaM Tech"):
        self.name = name
        self.age = age
        self.branch = branch
        self.sem = sem
        self.clg = clg

    def printDetails(self):
        print("Student Details !!!")
        print(f"Name of the student : {self.name} , Age of the student : {self.age} , College of the student : {self.clg} , Branch of the student : {self.branch} , Semester of the student : {self.sem}")


std1 = Student("Retro", 20, "AIT", "AI", 8)
std1.printDetails()   

print("\n")

std2 = Student("Sai", 24, "IIT", "ic",10)
std2.printDetails()
print("\n")

std3 = Student("Sanket", 26, "AIhhh", 3)
std3.printDetails()


#object creation
#objectName=ClassName()
#objectName.methodName()
    

