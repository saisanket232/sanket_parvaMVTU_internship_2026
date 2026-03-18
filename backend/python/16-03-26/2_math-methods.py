#Methods: min,max,abs,pow

numbers = [2,7,3,5,9,6]

#min
minValue = min(numbers)

#max
maxValue = max(numbers)

print(f"Min value: {minValue}, Max value: {maxValue}")

#abs
negative = [-3,2,-5,4]
for num in negative:
    print(abs(num))

#pow
print(f"5^2: {pow(5,2)}")

#Math Module Methods: sqrt, sin, cos, tan, ceil, floor, isnan, issqrt, prod, remainder

import math

#sqrt
print(f"Square Root of 25: {math.sqrt(25)}")

#issqrt
print(f"Square Root of 27: {math.isqrt(27)}")

#ceil & floor
#ceil rounds a number up to the nearest integer, while floor rounds a number down to the nearest integer.
#floor rounds down to the nearest integer, while ceil rounds up to the nearest integer. For example, math.floor(2.75) would return 2, while math.ceil(2.75) would return 3.
number = 2.75
print(f"Cell Value of {number}: {math.ceil(number)}")
print(f"Floor Value of {number}: {math.floor(number)}")

#sin, cos, tan
print(f"Sine of 90: {math.sin(90)}")
print(f"Cos of 90: {math.cos(90)}")
print(f"Tan of 90: {math.tan(90)}")

#remainder
print(f"You need {math.remainder(32,7)} to divide 31 completly by 3")

#math constants: pi, e, tau, inf, nan
print(f"Value of Pi: {math.pi}")
print(f"Value of e: {math.e}")
print(f"Value of Tau (2*pi): {math.tau}")
print(f"Value of Infinity: {math.inf}")
print(f"Value of NaN: {math.nan}")

#isnan
print(f"Is NaN: {math.isnan(math.nan)}")

#radius and degree conversion
angle = 180
print(f"Angle in Radians: {math.radians(angle)}")
print(f"Angle in Degrees: {math.degrees(math.pi)}")

#math.sin(),math.cos(),math.tan()
angle = math.radians(90)
print(f"Sine of 90 degrees: {math.sin(angle)}")
print(f"Cosine of 90 degrees: {math.cos(angle)}")
print(f"Tangent of 90 degrees: {math.tan(angle)}")

#GCD
print(f"GCD of 48 and 18: {math.gcd(48,18)}")

#Factorial
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Factorial of 10: {math.factorial(10)}")

# fabs -float absolute value
print(f"Absolute value of -3.5: {math.fabs(-3.5)}")

print(f"Absolute value of -0.5: {abs(-0.5)}")


#product of a list of numbers
print(f"Product of 2,3,4: {math.prod([2,3,4])}")

