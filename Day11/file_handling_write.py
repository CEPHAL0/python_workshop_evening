# Open the file for writing
f = open("greetings.txt", "w")

f.write("Hello, I am writing this through python code into the file")

f.close()

# Open the file again for reading
f = open("greetings.txt", "r")

content = f.read()

print(content)

f.close()