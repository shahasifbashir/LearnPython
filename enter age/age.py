#Program to teel a users in how many years they will become 100
print("Hello")
print("Please enter your name")

# ask for the name
name = input()

print("Okay {} enter your age".format(name))

#ask for the age
age = int(input())
hundredIn = 100-age

print("{} you will become 100 in {} years".format(name,hundredIn))