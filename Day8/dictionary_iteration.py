# for loop for dictionaries

personal_information = {
    "name": "Sharad",
    "address": "Kathmandu",
    "gender": "Male",
    "college": "DWIT"
}

print(personal_information.keys())

# # Just access the key from dictionary
for key in personal_information.keys():
    # key
    print(key)
    print(personal_information[key])

for key, value in personal_information.items():
    print(f"{key}: {value}")