#While Loop
#Break and Continue
number = 0
for n in [1,2,3,4,5,6,7]:
    if n == 5:
        break
    print(n)

while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)