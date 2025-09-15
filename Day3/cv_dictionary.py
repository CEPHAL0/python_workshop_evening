cv = {}

cv["name"] = input("Enter the name: ")
cv["profession"] = input("Enter the profession: ")
cv["phone-number"] = input("Enter the phone number: ")

# Print the dictionary
print(cv)

# Access the dictionary elements and print a message
print(f'{cv["name"]} is a {cv["profession"]}')

# Print the CV in a proper format
print(f"""
----------
CV
----------
Name: {cv["name"]}
Profession: {cv["profession"]}
Phone Number: {cv["phone-number"]}
""")