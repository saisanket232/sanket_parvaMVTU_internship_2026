class NumberOps:
    def __init__(self, num):
        self.num = num

    def count_digits(self):
        temp = self.num
        count = 0

        while temp > 0:
            count += 1
            temp //= 10

        return count

    def sum_digits(self):
        temp = self.num
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit
            temp //= 10

        return total

    def is_palindrome(self):
        temp = self.num
        rev = 0

        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10

        return self.num == rev

    def is_armstrong(self):
        count = self.count_digits()

        temp = self.num
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** count
            temp //= 10

        return total == self.num

    def is_strong(self):
        temp = self.num
        total = 0

        while temp > 0:
            digit = temp % 10
            fact = 1

            for i in range(1, digit + 1):
                fact *= i

            total += fact
            temp //= 10

        return total == self.num


# main
num1 = int(input("Enter a number: "))
obj1 = NumberOps(num1)
num2 = int(input("Enter a number: "))
obj2 = NumberOps(num2)

d1 = obj1.count_digits()
d2 = obj2.count_digits()

if d1 > d2:
    print(f"{num1} has more digits than {num2}")
elif d1 < d2:
    print(f"{num2} has more digits than {num1}")
else:
    print(f"{num1} and {num2} have the same number of digits")

s1= obj1.sum_digits()
s2= obj2.sum_digits()
print("Digits:", d1, d2)
print("Sum:", s1, s2)

print(f"{num1} Palindrome:", obj1.is_palindrome())
print(f"{num2} Palindrome:", obj2.is_palindrome())

print(f"{num1} Armstrong:", obj1.is_armstrong())
print(f"{num2} Armstrong:", obj2.is_armstrong())

print(f"{num1} Strong:", obj1.is_strong())
print(f"{num2} Strong:", obj2.is_strong())

