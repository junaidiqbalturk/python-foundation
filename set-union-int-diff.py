#Set Union
#Set Intersection
#Set Difference

lettersA = {"A","B","C","D"}
lettersB = {"E","F","A","D"}
#Set Uniono
union = lettersA | lettersB
#Intersection
intersection = lettersA & lettersB
#Difference
difference = lettersA - lettersB
print(f"union = {union}")
print(f"intersection = {intersection}")
print(f"difference = {difference}")
