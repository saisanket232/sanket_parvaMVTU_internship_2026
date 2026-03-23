students = {
    1: {"name": "Sai", "marks": [80, 85, 90]},
    2: {"name": "Sagar", "marks": [70, 75, 78]},
    3: {"name": "Reddy", "marks": [88, 92, 95]}
}

students[1]["marks"].append(88)
students[2]["marks"].append(86)
students[3]["marks"].append(89)

# Add average
for student in students.values():
    student["average"] = sum(student["marks"]) / len(student["marks"])

# Find topper
topper = max(students, key=lambda x: students[x]["average"])
print("Topper:", students[topper]["name"])

# Find lowest
lowest = min(students, key=lambda x: students[x]["average"])

# Delete lowest
students.pop(lowest)

print("Updated Students:", students)

#next

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

for i in range(1,5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

num33=int(input("Enter the Number : "))

num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed:", rev)

