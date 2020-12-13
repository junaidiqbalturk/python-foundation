#Lists in Python
numbers = [1,2,3,4,-1,-20,["A","B","C"]]

print(numbers)
print(numbers[0])  #Index 0
print(numbers[1])  #Index 1
print(numbers[2])   #Index 2
print(numbers[3])  #Index 3
print(numbers[4]) #Index 4
print(numbers[5])  #Index 5
print(numbers[6][0]) #Index 6 Of 0 since theres a list in a list
print(numbers[6][1]) #Index 6 Of ``1`` since theres a list in a list
print(numbers[6][2]) #Index 6 Of ``2`` since theres a list in a list

#METHODS IN LISTS

num = [1,2,4,3]
num.sort()  #Sorting
num.reverse() #Reverse the list
num.append(1000) #Appending the list
# print(-10 in num)   #Return Boolean to check whether number is in the list or not
num.remove(1)  #Remove Items from the list
num.pop()      #Remove from the top of the list
del num[0]  #delete item at index 0
del num[0:2] #delete item from index 0 to 2
print(num)