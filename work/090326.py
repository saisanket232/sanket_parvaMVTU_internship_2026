fname="Sai"
lname="Sanket"
print(fname + " " + lname+" M")

age=24
height=5.7
is_student=True

print("Age is :",age ,",", type(age))
print("Height is :",height,",",type(height))
print("Student :",is_student,",",type(is_student))

#Basic Calculator

n1=40
n2=50

n3=n1+n2
n4=n1-n2
n5=n1*n2
n6=n1/n2
n7=n1**3
n8=n1%n2

print("Addition is :",n3)
print("Subtraction is :",n4)
print("Multiplication is :",n5)
print("Division is :",n6)
print("Exponentiation is :",n7)
print("Modulus is :",n8)


number=69

number+=96
print("After addition :",number)
number-=69
print("After subtraction :",number)
number*=2
print("After multiplication :",number)
number/=2
print("After division :",number)
number//=2
print("Final number is :",number)

num1=70
num2=30

print("num1 > num2 :",num1 > num2)

yes=num1<num2
print("num1 < num2 :",yes)

print("x <= y :",num1 <= num2)
print("x >= y :",num1 >= num2)
print("x == y :",num1 == num2)  
print("x != y :",num1 != num2)

dell=90

print("dell > 80 and dell < 100 :",dell > 80 and dell < 100)
print("and :",dell > 10 and dell%5==0)
print("or :",dell > 10 or dell/3==0)
print("not :",not(dell > 80 and dell < 100))

fruits=["Apple","Banana","Mango"]
print("Fruits :",fruits)

fruits.append("Orange")
print("Fruits.append :",fruits)

fruits.insert(1,"Grapes")
print("Fruits.insert :",fruits)

fruits.remove("Banana")
print("Fruits.remove :",fruits)

fruits.reverse()
print("Fruits.reverse :",fruits)

fruits.sort(reverse=True)
print("Fruits.sort :",fruits)

hi=fruits.index("Apple")
print("Index :",hi)

book = ["Python", "Java", "C++"]

book.append("JS")
print("Book is :",book)

book.insert(3,"SQL")
print("Book.insert is :",book)

book.remove("C++")
print("Book.remove is :",book)

print("Book is :",len(book))
# ss=book.index[0]
# sss=book.index[3]
# print("Book 1 and last:",ss,sss)

print("First book:",book[0])
print("Last book:",book[-1])
languages = ["Python", "Java", "C++", "Go"]

print("Python" in languages)
print("Rust" in languages)
print("Java" not in languages)

numbers = [10,20,30,40,50,60]

print("Numbers:",numbers[:3])
print("Numbers:",numbers[4:])
print("Numbers:",numbers[2:5])
print("Numbers:",numbers[::2])
