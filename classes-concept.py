#Lets Uderstand the concept of Classes in Python
#CLass is a blue print
class Phone:
    def __init__(self, brand, price):  # Parameterized Constructor
        self.brand = brand
        self.price = price

#Behavior Function
    def call(self, phone_number):
        print(f"{self.brand} is Calling {phone_number}")

#Override Object Print Method
    def __str__(self) -> str:
        return f"Brand {self.brand} Price ={self.price}"

#-> this arrow in the above function represents
# that this function will return a string
#we can remove that arrow as well but its okay to define the return type


iphone = Phone("Iphone 7+",300)  #Objects
samsung = Phone("Samsung S20",1400)  #Individual Objects

print(iphone)
iphone.call("999")

print(samsung)
samsung.call("1234")

#Conventional Methods for Printing Objects in Python
print(iphone.brand)
print(iphone.price)
iphone.call("999")
#Conventional Methods for Printing Objects in Python
print(samsung.brand)
print(samsung.price)
samsung.call("1234")