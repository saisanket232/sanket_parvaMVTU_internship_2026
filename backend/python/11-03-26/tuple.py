# Tuples in Python
# A tuple is an ordered, immutable collection of items. It is defined using parentheses ().
# Creating tuples
fruits = ("apple", "banana", "orange")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Accessing elements
print(fruits[0])  # apple
print(numbers[-1])  # 5

# Unpacking tuples
a, b, c = fruits
print(a, b, c)

# Iterating through tuples
for fruit in fruits:
    print(fruit)

# Tuple methods
print(fruits.count("apple"))  # 1
print(numbers.index(3))  # 2

# Tuples are immutable (cannot be changed)
# fruits[0] = "mango"  # This would raise an error