import pickle

data = {"name": "Sharad", "address": "Kathmandu", "gender": "Male"}

f = open("dictionary_dump.pkl", "wb")
pickle.dump(data, f)
f.close()

f = open("dictionary_dump.pkl", "rb")
loaded_dictionary = pickle.load(f)
print(type(loaded_dictionary))
print(loaded_dictionary)
f.close()