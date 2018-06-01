#list comprhension doing a lot in a single line of code

A = [1,2,3,4,5,5,6,7,7,5,3,5,2,34,4,4,5,56,6,7,7,6,6,54,6,3,3,45,5,6,6,6,6,65,8,4,4,44,10]

#The below code returns the elements that are only even
print([item for item in A if item%2 ==0])
