#Creating Files

#Files Flag
#w for writing
# a for appending
# r for reading
# r+ for reading and writing

file = open("./data.csv","r+")
file.write("ID,Name,email\n")
file.write("1,Jamila,jamila@gmail.com\n")
file.write("2,Jamila,alex@gmail.com\n")
file.write("3,Junaid,junaid@gmail.com\n")
file.close()

