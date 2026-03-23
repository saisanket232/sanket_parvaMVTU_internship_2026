students = {
    "Sai": [80, 90, 85],
    "Sagar": [70, 60, 75],
    "Reddy": [95, 92, 93],
    "Ajay": [50, 65, 55]
}

topper_name = ""
max_avg = 0
failed_students = []

for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)

    # Grade assignment
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "Fail"

    # Update student data (replace list with dictionary)
    students[name] = {
        "marks": marks,
        "total": total,
        "average": avg,
        "grade": grade
    }

    # Find topper
    if avg > max_avg:
        max_avg = avg
        topper_name = name

    # Find failed students
    if avg < 60:
        failed_students.append(name)

print("Students Data:", students)
print("Topper:", topper_name)
print("Failed Students:", failed_students)


##loop+logic

num1 = input("Enter number: ")
print(len(num1))

#divide by 10 (integer division)
num = int(input("Enter number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Digits:", count)

num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n