def my_intro():
    print("Name : Retro")
    print("Age : 234")
    print("City : Krt")
my_intro()

def multiply(a,b):
    print("Result of multiply :",a*b)
multiply(4,6)

def multiply(a,b):
    print("Result of multiply :")
    return a*b
xx=multiply(4,6)
print(xx)

def rectangle_area(l,b):
    print("The Area of Rectangle :")
    return l*b
lb=rectangle_area(6,8)
print(lb)

def coffee(type, sugar=1):
    print(f"Making {type} with {sugar} sugar")
coffee("Coffee")
coffee("Sugar")

def employee(name,department,salary):
    print(f"Name : {name}, Department : {department}, Salary : {salary}")
    
employee("Sai","CSE",1000000)


def my_fruits(*fruits):
    print(fruits)
my_fruits("Apple",'banana','kiwi')

def phone_specs(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():    
        print(f"{key}:{value}")
phone_specs(name='sagar',phone=8888888)

discount=lambda x : x-x*.1
# print(discount(1000))
x=1000
print(discount(x))

def countdown(n):
    if n == 0:
        print("Countdown finished!")
    else:
        print(n)
        countdown(n-1)

countdown(5)

counter = 0
def increment():
    global counter
    counter += 1
    print(f"Counter: {counter}")
increment()
increment()
increment()