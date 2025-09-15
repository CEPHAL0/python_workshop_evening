complex_dict = {
    "name": "Sharad",
    "address": {
        "province": "Bagmati",
        "district": "Kathmandu",
        "municipality": "Kathmandu",
    },
    "hobbies": ["Gardening", "Boutique", "Music"],
}

province_name = complex_dict["address"]["province"]

complex_dict["address"]["district"] = "Bhaktapur"
complex_dict["address"]["ward"]= 24

print(complex_dict)
print(complex_dict["hobbies"][0])
print(province_name)