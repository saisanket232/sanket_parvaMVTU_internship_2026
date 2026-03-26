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
            total += temp % 10
            temp //= 10

        return total


# Step 1: Create list
objs = []

n = int(input("How many numbers: "))

# Step 2: Loop + object creation
for i in range(n):
    num = int(input("Enter number: "))
    obj = NumberOps(num)
    objs.append(obj)


# Step 3: Max digits
max_digit_obj = objs[0]

for obj in objs:
    if obj.count_digits() > max_digit_obj.count_digits():
        max_digit_obj = obj


# Step 4: Max sum
max_sum_obj = objs[0]

for obj in objs:
    if obj.sum_digits() > max_sum_obj.sum_digits():
        max_sum_obj = obj


print("Max digits number:", max_digit_obj.num)
print("Max sum number:", max_sum_obj.num)