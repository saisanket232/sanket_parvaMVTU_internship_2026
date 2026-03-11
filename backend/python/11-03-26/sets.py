# {}

#set properties :
#unordered,unchangeble,Do Not alllow Duplicated


multiplesof2={2,4,6,8,10,10}
print(multiplesof2,type(multiplesof2))

#true and 1 -considered as same value ,false and 0 are same

randomSet={1,False,0,True}
print(randomSet)

#Sets Methods

#union, intersection,Difference,copy,difference_update,intersection_update,isdisjoint,issubset,issuperset,pop,remove,symmetric_difference,symmetric_difference_update,update,clear,add

set1={3,5,8,2,22,66,69}
set2={6,8,2,5,5,7,8,29,99,33,100}

print("Set1 :",set1)
print("Set2 :",set2)

# print(set1.union(set2)) |
set3=set1.union(set2)
print("union :",set3)
#&
set4=set1.intersection(set2)
print("Intersection :",set4)
set5=set1.difference(set2)
print("Difference 1 :",set5)

set1.difference_update(set2)
print("Diff_update:",set1)
set6=set2.difference(set1)
print("Difference 2 :",set6)
# set1.intersection_update(set2)
# print("Intersection Update:",set1)

print("Isdisjoint :",set1.isdisjoint(set2))
print("Issubset :",set1.issubset(set2))
print("^ :",set1^set2)

# add() - Adds an element to the set
set1.add(100)
print("After add(100):", set1)

# clear() - Removes all elements from the set
set_temp = {1, 2, 3}
set_temp.clear()
print("After clear():", set_temp)

# copy() - Returns a copy of the set
set_copy = set2.copy()
print("Copy of set2:", set_copy)

# discard() - Remove the specified item
set2.discard(6)
print("After discard(6):", set2)

# pop() - Removes an arbitrary element from the set
set_temp2 = {10, 20, 30}
removed = set_temp2.pop()
print("After pop():", set_temp2, "removed:", removed)

# remove() - Removes the specified element
set2.remove(7)
print("After remove(7):", set2)

# symmetric_difference() - Returns set with symmetric differences
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric difference:", sym_diff)

# symmetric_difference_update() - Updates with symmetric differences
set_a.symmetric_difference_update(set_b)
print("After symmetric_difference_update:", set_a)

# update() - Updates the set with union of sets
set_c = {100, 200}
set_d = {300, 400}
set_c.update(set_d)
print("After update():", set_c)

# issuperset() - Returns True if all items of another set are present
set_x = {1, 2, 3, 4, 5}
set_y = {2, 3}
print("Is set_x superset of set_y:", set_x.issuperset(set_y))