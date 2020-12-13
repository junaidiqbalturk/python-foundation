#Reading through Files correct way
import os.path
#Check first if file exists or npt

filename = "data.csv"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")


#This is the correct way to work with file because
#through this we dont have to write file.close everytime we tr to access the file
