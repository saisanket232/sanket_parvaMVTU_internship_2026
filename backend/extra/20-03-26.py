students = {
    1: {"name": "Sai", "age": 21, "skills": ["Python"], "marks": 85},
    2: {"name": "Sagar", "age": 22, "skills": ["Java"], "marks": 78},
    3: {"name": "Reddy", "age": 23, "skills": ["C++"], "marks": 90}
}

students[4] = {"name": "Ajay", "age": 20, "skills": ["HTML"], "marks": 88}


students[2]["marks"] = 90
print(students)

hi=students.get(1)
print(hi)

students.pop(3)
print(students)

for student in students.values():
    print(student)

#loop
for key, value in students.items():
    print(f"Student ID: {key}")
    print(f"Name: {value['name']}")
    print(f"Age: {value['age']}")
    print(f"Skills: {', '.join(value['skills'])}")
    print(f"Marks: {value['marks']}")
    print()

for i in range(1,51):
    if i%2==0:
        print(f"{i} is even")
    # else:
    #     print(f"{i} is odd")

for i in range(1,101):
    if i%7==0:
        print(f"{i} is multiple of 7")

for i in range(1,21):
    if i%2==0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
   

num=int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

num2=int(input("Enter a number: "))
h22=fact(num2)
print(h22)