f = open("test.txt", "r")
print(f.read())
f.close()


# Shorthand for above code
with open("test.txt", "r") as f:
    print(f.read())


with open("test.txt", "w") as f:
    f.write()