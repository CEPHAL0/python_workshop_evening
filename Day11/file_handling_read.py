# File Handling
# Interaction with External Files
# Read, Write, Create, Delete, Update, Overwrite

# Reading through python in external files

# Modes
# Write -> w
# Read -> r
# Append -> a
# Create -> x

# Open
f = open("test.txt", "r")

content = f.read()
print(content)

# Cursor is at the end, so no data is retrieved
# content = f.read()
# print(content)

# Close
f.close()



# Reading a specific number of characters
f = open("test.txt", "r")

first_5_letters = f.read(5)
print(first_5_letters)

next_5_letters = f.read(5)
print(next_5_letters)

f.close()

# Reading Lines
f = open("test.txt", "r")

print(f.readline())
print(f.readline())
print(f.readline())

# no 4th line, hence empty output
print(f.readline())

f.close()