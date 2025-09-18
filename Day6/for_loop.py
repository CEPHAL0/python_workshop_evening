fruits = ["Apple", "Banana", "Guava", "Orange"]
names = ["John", "Alice", "Mike"]

# Simplest form of for loop
for fruit in fruits:
    print(fruit)

# Nested for loop
for name in names:
    for fruit in fruits:
        print(f"{name} has {fruit}")

marks = [45, 54, 66, 77, 89]

# Calculate the sum of marks
sum_marks = 0
for m in marks:
    sum_marks = sum_marks + m

print(sum_marks)

# String as a list of characters
city = "Kathmandu"
pattern = ""
for a in city:
    pattern = pattern + a
    print(pattern)

fruits = ["Apple", "Banana", "Guava", "Mango"]

for index, value in enumerate(fruits):
    remainder = index % 2
    if remainder == 0:
        print(f"{index}: {value}")


number_of_times = int(input("Enter the number of times: "))
temp_list = range(1, number_of_times+1)
for item in temp_list:
    print(f"Hello {item} times")

for item in range(10):
    print(item)


# Different versions of range
range(10)  # Stop
range(1, 10)  # Start and Stop
range(1, 10, 2)  # Start, Stop and Step

# Positive Skipping
for item in range(1, 10, 2):
    print(item)

#  Negative Skipping
for item in range(10, 1, -2):
    print(item)

# Perform the repetitive tasks
marks = []
for i in range(5):
    input_marks = int(input(f"Enter the marks of subject {i}: "))
    marks.append(input_marks)

print(marks)