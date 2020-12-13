#Loops in Python allows us to iterate through set lists, dictionaires, or any data structure available
#For Loops
names = ["Ahmed","Junaid","Annah",
         "James","Jamila"]
#For Loop
for name in names:
    print(name)

#How to Loop through Dictionaries
person = {
    "name": "Junaid",
    "Age" : 20,
    "Addresss": "Karachi,Pakistan"
}
for key, value in person.items():
    print(f"Key:{key} value:{value}")

#ALTERNATE METHOD FOR ITERATING DICTIONARIES
# for key in person:
#     print(f"Key:{key} value:{person[key]}")