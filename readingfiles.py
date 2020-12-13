#Reading through Files

file = open("./data.csv","r")

# print(file.read())

# print(file.read())

for line in file:
    print(line)

file.close()