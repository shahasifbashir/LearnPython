# A simple list
myList = [10,20,4,5,6,2,9,10,2,3,34,14]

#print the whole list

print("The List is {}".format(myList))

# printing elemts of the list one by one

print("printing elemts of the list one by one")
for elements in myList:
    print(elements)

print("")

#printing elements that are greater than 10 only

print("printing elements that are greater than 10 only")

for elements in myList:
    if(elements>10):
        print(elements)

#printing elements that are greater that 10 but by using a list and appending the elements on it

newList = []

for elements in myList:
    if(elements <10):
        newList.append(elements)

print("")
print("Print the new List \n{}".format(newList))

#print the above list part using a single line

print(" The list is {}".format([item for item in myList if item < 10]))

# here [item { This is the out put} for item { the is the for part} in myList {This Is the input list} if item <10 {This is the condition}]

#Ask the user for an input and print the elemets of list less than that number
print("Input a number : ")
num = int(input())

print(" The elemnts of the list less that {} are {}".format(num,[item for item in myList if item < num]))
