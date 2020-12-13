#Dictionaries
#Dictionaires allows you to store key value pair
#Dictionaires are very helpful when you have a structured data
person = {
    "name": "Junaid",
    "Age" : 20,
    "Addresss": "Karachi,Pakistan"
}

print(person["name"])
print(person["Age"])
print(person["Addresss"])

#Methods Related to Dictionaries
# print(person.keys())
# print(person.values())
# print(person.clear())
print(person.get("Age"))
person["Age"] = 100
print(person)
