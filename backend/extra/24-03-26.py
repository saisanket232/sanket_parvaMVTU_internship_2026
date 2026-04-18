 #reverse the number

#% (Modulus Operator)
#This gives the remainder after division

#input=12345
#output=54321

#1
hello = int(input("Enter the number: "))
original = hello   # store original number
reverse = 0

while hello > 0:
    num = hello % 10
    reverse = reverse * 10 + num
    hello = hello // 10

print(f"The reversed number is: {reverse}")
#2
if original == reverse:
    print(f"{original} is Palindrome")
else:
    print(f"{original} is not Palindrome")

#3

hi = int(input("Enter the number: "))
count1 = 0
count2 = 0
sum1=0
sum2=0

while hi > 0:
    num1 = hi % 10
    
    if num1 % 2 == 0:
        count1 += 1
        sum1+=num1
    else :
        count2+=1
        sum2+=num1

    hi = hi // 10

print(f"The number has {count1} even digits")
print(f"The number has {count2} odd digits")

print(f"The sum number has {sum1} even digits")
print(f"The sum number has {sum2} odd digits")

#4

num4 = int(input("Enter the number: "))

largest = -1
second_largest=-1
smallest =10
second_largest=10
if num4==0 or num4<0:
    print(f"The number is invalid")
else:
    while num4 > 0:
        digit = num4 % 10
        if  digit> largest:
            second_largest = largest
            largest =digit
        elif digit > second_largest and digit != largest:
            second_largest=digit
        elif digit<smallest:
            smallest=digit
        elif digit < second_largest and digit != largest:
            second_largest=digit
        num4 = num4 // 10

print(f"The largest digit is: {largest}")
print(f"The Second largest digit is: {second_largest}")

#5

num5 = int(input("Enter the number: "))

wel = num5

# Step 1: count digits
temp = num5
count = 0

while temp > 0:
    count += 1
    temp = temp // 10

# Step 2: Armstrong calculation
total = 0

while num5 > 0:
    digit = num5 % 10
    total += digit ** count
    num5 = num5 // 10

# Step 3: check
if wel == total:
    print(f"{wel} is an Armstrong number")
else:
    print(f"{wel} is not an Armstrong number")

#6
#strong number

num6 = int(input("Enter the Number: "))

sn = num6
tt = 0

while num6 > 0:
    digit = num6 % 10

    # find factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    tt += fact
    num6 = num6 // 10

if tt == sn:
    print(f"{sn} is a Strong number")
else:
    print(f"{sn} is not a Strong number")