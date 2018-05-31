import random
#This Examples gives the union of two Lists

A = [1,2,3,4,5,6,7,8,5,4,3,3,6,7,8]
B=[6,7,8,9,4,3,5,6,78,97,2,3,4,5,5,6,7,7,8]

# we will use the set becouse a set contains unique elemets only ann then use an and operator

print(list(set(A)&set(B)))

# The same example using Random Lists
A= range(1,random.randint(1,30))
B= range(1,random.randint(1,40))

print("_____________________________")
print(list(set(A)&set(B)))
myList=[]
# Ths same example using a for loop

for item in A:
    if item in B:
        if item not in myList:
            myList.append(item)
print(myList)
