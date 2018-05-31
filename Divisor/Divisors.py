#This program asks user for a number and the outputs all the divisors of that number
#Ask user for a n input
num = int (input("Input an integer : "))
# now create a list of all possible divisors

myList = range(2,(num//2+1))

for item in myList:
    if(num%item==0):
        print(item,end=" ")

print(num)
