# Initialization
marks =[10, 20, 30, 40]

# Indexing
# 1st Element
first_element = marks[0]
print(first_element)

# Error
# print(marks[9])

# To calculate the length of list
number = len(marks)
print(number)

# Fetch the last element from list
last_number = number - 1
last_element = marks[len(marks)-1]
print(last_element)

# Fetch the last element without length
last_number = marks[-1]
print(last_number)

# Calculate the sum of the items from lists
sum = marks[0] + marks[1] + marks[2] + marks[3]
print(sum)

# Add Items into list
marks.append(50)
print(marks)
print(marks[-1])

# Change the value of existing items
marks[1] = 90
print(marks)

# Delete the items from list

# remove() function
marks.remove(10) # Removing by value
print(marks)

# pop() function
marks.pop(0) # Removing by index
print(marks)

names = ["Sharad", "John", "Alice"]
names[0] = "Saroj"
print(names)

names.remove("John")
print(names)

names.pop(1)
print(names)
