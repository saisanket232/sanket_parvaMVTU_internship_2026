#1
data = {
    "math": 80,
    "science": 90,
    "english": 70
}

for key ,value in data.items():
    print(key,value)

#2
total=0
numm={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10
}

for value in numm.values():
    total+=value
print(total)

#3
subjects={
    "A":"Math",
    "B":"Science",
    "C":"English",
    "D":"History",
    "E":"Geography"
}

for key in subjects.keys():
    print(key)

#4
monkey={
    "math":79,
    "science":89,
    "english":76,
    "history":69
}

for key,value in monkey.items():
    if value>80:
        print(key)

#5
data = {
    "a": 10,
    "b": 25,
    "c": 5,
    "d": 30
}
count=0
for key,value in data.items():
    if value>10:
       count+=1
print(count) 

#6
scores={
    "math":80,
    "science":90,
    "english":70
}
new_dict = {}

for key, value in scores.items():
    new_dict[key] = value * 2

print(new_dict)
#7

scores = {
    "math": 80,
    "science": 90,
    "english": 70
}

max_value = 0
max_key = ""

for key, value in scores.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key, max_value)

#8
data = {
    "a": 1,
    "b": 2
}

reversed_dict = {}
for key,value in data.items():
    reversed_dict[value] = key

print(reversed_dict)

#9
students = {
    "Sanket": {"math": 80, "science": 90},
    "Rahul": {"math": 70, "science": 60}
}

for name, marks in students.items():
    total = 0
    
    for subject, score in marks.items():
        total += score
    
    print(name, total)
#10
data = {
    "a": 10,
    "b": 25,
    "c": 5
}

highest = 0
highest_key = ""

for key, value in data.items():
    if value > highest:
        highest = value
        highest_key = key

print(highest_key, "has highest value")