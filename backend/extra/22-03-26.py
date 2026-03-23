num = int(input("Enter number: "))
count = 0

if num > 0:
    while num > 0:
        num = num // 10
        count += 1
    # print(count) is now properly indented inside the if block
    print(count)
else:
    print("Enter a valid number")

#2
num=int(input("Enter number: "))
rev=0

while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

#3
num2=int(input("Enter the sum of digits :"))
sum=0

for i in range(num2):
    sum=sum+i
print(sum)

#4
num3=int(input("Enter number for even or odd: "))
if num3%2==0:
    print(f"The Number is Even:{num3}")
else:
    print(f"The Number is Odd:{num3}")

#5

for i in range(1,4):
    num5=int(input("Enter number: "))
    
print(max(num5))


#6
num6=int(input("Enter number: "))
palindrome=num6

while num6>0:
    digit=num6%10
    palindrome=palindrome*10+digit
    num6=num6//10

if palindrome==num6:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")

#7
num7=int(input("Enter number: "))
fib=num7
a=0
b=1

while num7>0:
    if num7==0:
        print("The number is not a fibonacci number")
    elif num7==1:
        print("The number is a fibonacci number")
    else:
        for i in range(num7):
          print(a, end=" ")
          a, b = b, a + b 

#8
num8=int(input("Enter number: "))
fact=0

while num8>0:
    def fact(n):
        if n==0:
            print("The number is not a factorial number")
        else:
            fact=n*fact(n-1)
        return fact
print(fact(num8))

#9
letter=input("Enter the letter:")

if letter in "aeiouAEIOU":
    print("The letter is a vowel")
else:
    print("The letter is a consonant")

#10
lists=list(map(int,input("Enter the numbers: ").split()))

print(max(lists))


#11
num11 = int(input("Enter number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num11):
        if num11 % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

