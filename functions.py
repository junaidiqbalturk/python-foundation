#Functions in Python
def greeting(name,age=-1):
    print(f"Hello {name} How are you?")
    if not age < 0:
        print(f"I Know you are {age} old")

greeting("Junaid")
greeting("Alex",22)

#Return values from Function
def is_adult(age):
    if age >= 16:
        return True;
    else:
        return False;

def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == 'F':
        return "Female"
    else:
        return f"gender {gender} is unknown"

result = is_adult(30)
print(result)
print(convertGender('F'))
print(convertGender('M'))
print(convertGender('f'))
print(convertGender('m'))
print(convertGender('Hello'))