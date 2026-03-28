#Operator Overloading
# """Operator overloading is a feature in Python that allows you to redefine the behavior of operators for custom objects."""

#2 ways
#1)Built-in methods
#2)Operator overloading(special methods-dunder methods)

#Built-in methods
class Addition:
   def add(self,op1,op2):
      print(f"The sum of {op1} and {op2} is {op1+op2}")

add = Addition()
#integer Addition
add.add(10,20)
#string Addition
add.add("Hello ","World")
#float Addition
add.add(10.5,20.5)

#Operator overloading(special methods-dunder methods)
class Addition:
   def __add__(self,op1,op2):
      print(f"The sum of {op1} and {op2} is {op1+op2}")

add = Addition()
add.__add__(10,20)

# "*"

class Multiplication:
    def mul(self,op1,op2):
        print(f"The product of {op1} and {op2} is {op1*op2}")

multiply = Multiplication()
multiply.mul(10,20)
multiply.mul("Hello ",3)
multiply.mul(10.5,20.5)

#"in"-membership operator

class Membership:
    def contains(self,item):
        return item in self.items

membership = Membership()
membership.items = [1,2,3,4,5]
print(membership.contains(3))

#membership.check(5,[1,2,3,4,5])
#"not in"-membership operator

class Membership:
    def not_contains(self,item):
        return item not in self.items

membership = Membership()
membership.items = [1,2,3,4,5]
print(membership.not_contains(3))

#> or <

class Comparison:
    def gt(self,other):
        print(self.value > other)

comparison = Comparison()
comparison.value = 10
comparison.gt(5)
print(comparison.gt(5))

#Indexing Operator[]

class Index:
    def display(self,value,index):
        print(f"The value at index {index} is {value[index]}")

index = Index()
index.display([1,2,3,4,5],2)

#Magic Methods
#"__init__"-constructor

class Magic:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return self.value + other.value

    def __gt__(self,other):
        return self.value > other.value

    def __lt__(self,other):
        return self.value < other.value

magic1= Magic(10)
magic2 = Magic(20)
print(magic1 + magic2)
print(magic1 > magic2)
print(magic1 < magic2)


#__add__,__radd__,__gt__,__lt__,__mul__,__truediv__,__len__
#2

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print(f"Item Added to the cart: {self.name}")

    def __add__(self, other):
        # We need to explicitly check if 'other' is also a Product
        if isinstance(other, Product):
            return self.price + other.price
        # If 'other' is an integer/float (from a previous addition), just add it to the price
        elif isinstance(other, (int, float)):
            return self.price + other

    # Reverse Add (__radd__) is called when an integer is on the left side of the + operator
    # E.g., when doing product1 + product2 + product3 -> (30) + product3 -> 30.__add__(product3) flags an error,
    # so Python calls product3.__radd__(30) instead!
    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self,other):
        return self.price > other.price

    def __lt__(self,other):
        return self.price < other.price

    def total_cost(self):
        return self.price + self.price

product1 = Product("Apple",10)
product2 = Product("Banana",20)
product3 = Product("Orange",30)

#Products=[product1,product2,product3]
print(f"The sum of {product1.name} and {product2.name} is {product1 + product2}")
print(f"The greater of {product1.name} and {product2.name} is {product1 > product2}")
print(f"The less of {product1.name} and {product2.name} is {product1 < product2}")
print(f"The total cost of {product1.name} and {product2.name} is {product3.total_cost()}")

# Adding 3 Product Objects using the newly chained __add__ and __radd__ methods!
print(f"The sum of {product1.name}, {product2.name}, and {product3.name} is {product1 + product2 + product3}")

#3
#__str__,__len__,__setitem__,__getitem__

#__str__=to print in user friendly format
#__len__=to get the length of the object
#__setitem__=to set the value of the object
#__getitem__=to get the value of the object

class Emp:
    def __init__(self,name,age,emp_id,department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department
        print(f"Employee Added: {self.name},{self.age},{self.emp_id},{self.department}")

    # __str__ = to print in user friendly format
    def __str__(self):
        return f"Employee Name: {self.name}, Age: {self.age}, Emp ID: {self.emp_id}, Department: {self.department}"

    # __len__ = to get the length of the object (Returning the number of primary attributes: 4)
    def __len__(self):
        return 4

    # __getitem__ = to get the value of the object using bracket notation like emp["name"]
    def __getitem__(self, key):
        # Allow fetching attributes by string name via getattr
        if hasattr(self, key):
            return getattr(self, key)
        return f"Error: '{key}' not found"

    # __setitem__ = to set the value of the object using bracket notation like emp["age"] = 25
    def __setitem__(self, key, value):
        # Only allow setting existing attributes for safety
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            print(f"Error: Cannot set '{key}'. Attribute doesn't exist.")

emp1=Emp("Sai",21,101,"IT")
emp2=Emp("Sanket",22,102,"HR")
emp3=Emp("Retro",23,103,"Finance")

print(emp1)

# Testing the new magic methods!
print(f"Length of emp1: {len(emp1)}")
print(f"Getting emp1's age using __getitem__: {emp1['age']}")

# Setting the age using __setitem__
emp1['age'] = 99
print(f"emp1's updated age: {emp1['age']}")
