class Internship:
    #class variable,it is common for all the class members or objects
    company="ParvaM"
    #global variable
    duration="2 months"

    #instance variable
    def __init__(self,name,clg,branch,internship):
        self.name=name
        self.clg=clg
        self.branch=branch
        self.internship=internship

    def printDetails(self):
        print("Internship Details !!!")
        print(f"Name of the intern : {self.name} , College of the intern : {self.clg} , Branch of the intern : {self.branch} , Internship of the intern : {self.internship} ,At the duration of {self.duration} at {self.company}")

    def enroll(self):
        print(f"{self.name} has enrolled in {self.internship} internship at {self.company}")

    def joinclass(self):
        print(f"{self.name} has joined the class")

    def practice(self):
        print(f"{self.name} has started practicing {self.internship} concepts learned in class")

    def interview(self):
        print(f"{self.name} has attended the interview for industry exposure")


#self is automatically passed as an argument to the method
intern1=Internship("Sanket","AIT","AI","Python")
intern1.printDetails()
intern1.enroll()
intern1.joinclass()
intern1.practice()
intern1.interview()

print("\n")

intern2=Internship("Retro","AITTTT","cs","Java")
intern2.printDetails()
intern2.enroll()
intern2.joinclass()
intern2.practice()
intern2.interview()
print("\n")
#Example 2

class Car:
    # class variables
    mode_of_transport = "Road"
    no_of_wheels = 4

    def __init__(self, brand, model, fuel, price, color,mileage):
        self.carBrand = brand
        self.carModel = model
        self.carFuel = fuel
        self.carPrice = price
        self.carColor = color
        self.carMileage = mileage

    def demo(self):
        print("Car Details!!!")
        print(f"This is a {self.carBrand} brand and {self.carModel} model, "
              f"This is a car of {self.carFuel} fuel and {self.carPrice} price, "
              f"This is a car of {self.carColor} color and it is a {self.mode_of_transport} mode of transport "
              f"and it has {self.no_of_wheels} wheels")

    def drive(self):
        print(f"{self.carBrand} brand and {self.carModel} model is driving on the road")
    def park(self):
        print(f"{self.carBrand} brand and {self.carModel} model is parked")
    def parkCar(self):
        print(f"{self.carBrand} brand and {self.carModel} model is parked at {self.carPrice} price")
    def mileage(self):
        print(f"{self.carBrand} brand and {self.carModel} model is giving {self.carMileage+3} mileage")

car1=Car("Maruti","Swift","Petrol",800000,"Red",20)
car1.demo()
car1.drive()
car1.park()
car1.parkCar()
car1.mileage()
print("\n")

car2=Car("Tata","Nexon","Diesel",1000000,"Blue",18)
car2.demo()
car2.drive()
car2.park()
car2.parkCar()
car2.mileage()

# In OOPs ,we have 3 types of methods:
# 1. Instance methods
# 2. Class methods
# 3. Static methods

# 1. Instance methods:
# - methods that operate on instance variables
# - they take self as the first argument
# - they are called on an instance of the class
# - example- printDetails(), enroll(), joinclass(), practice(), interview(), demo(), drive(), park(), parkCar(), mileage()

#2. Class methods:
# - methods that operate on class variables
# - they take cls as the first argument
# - they are called on the class itself

#3. Static methods:
# - methods that operate on class variables
# - they take no arguments
# - they are called on the class itself

class Bank:
    #class variable
    bank_name="BOB"
    branch="Karatagi"
    no_of_accounts=0
    interest_rate=7.3

    def __init__(self,name,age,email,phone,address,typeOfAccount,balance):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
        self.address=address
        self.typeOfAccount=typeOfAccount
        self.balance=0
        Bank.no_of_accounts+=1

    #instance methods
    def createAccount(self):
        print(f"ThankYou for creating in {self.bank_name} bank account")

    def displayDetails(self):
        #random module is used to generate random numbers
        import random
        account_number=random.randint(1000000000,9999999999)
        print(f"Name of the account holder : {self.name} , Age of the account holder : {self.age} , Email of the account holder : {self.email} , Phone of the account holder : {self.phone} , Address of the account holder : {self.address} , Type of account : {self.typeOfAccount} , Balance of the account holder : {self.balance},Account number : {account_number}")

    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount {amount} has been deposited in your account")
        print(f"Balance of the account holder : {self.balance}")

    def withdraw(self,amount):
        self.balance-=amount
        print(f"Rs.{amount} has been withdrawn from your account")
        print(f"Balance of the account holder : {self.balance}")
    
    def checkBalance(self):
        print(f"Balance of the account holder : {self.balance}")

    #class methods
    #decorator-special symbol used for some purpose
    @classmethod
    def number_of_accounts(cls):
        print(f"Number of accounts in {cls.bank_name} bank : {cls.no_of_accounts}")

    @classmethod
    def calculateInterest(cls, amount, duration):
        print(f"Principal Amount:{amount}, Duration:{duration}, Interest Rate:{cls.interest_rate}")
        simpleInterest = (amount * duration * cls.interest_rate) / 100
        print(f"Simple Interest : {simpleInterest}")
        print(f"Total Amount : {amount + simpleInterest}")
    
    #static method- no arguments are passed, it is just a utility method
    @staticmethod
    def enquiry():
        print(f"ThankYou for contacting us at {Bank.bank_name} bank")

#New Account
cust1=Bank("Sanket",20,"sanket@gmail.com",9876543210,"123 Main St","Savings",0)
cust1.createAccount()
cust1.displayDetails()
cust1.deposit(1000)
cust1.withdraw(500)
cust1.checkBalance()
cust1.enquiry()
Bank.number_of_accounts()
Bank.calculateInterest(1000,2)
print("\n")

#New Account
cust2=Bank("Retro",30,"retro@gmail.com",9876543210,"123 Mg Road,Bangalore","Savings",3)
cust2.createAccount()
cust2.displayDetails()
cust2.deposit(10000)
cust2.withdraw(120)
cust2.checkBalance()
cust2.enquiry()
Bank.number_of_accounts()
Bank.calculateInterest(1500,1.5)