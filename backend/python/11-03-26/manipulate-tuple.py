states=("Kerala","Tamilnadu","Karnataka","Andhra Pradesh","Telangana")
print(states)
print(type(states))
# Convert tuple to list --list() function
statesList=list(states)
print(statesList)
print(type(statesList))

statesList.append("Goa")
print(statesList)

statesList.remove("Tamilnadu")
print(statesList)

states=tuple(statesList)
print(states)

print(states[::2])