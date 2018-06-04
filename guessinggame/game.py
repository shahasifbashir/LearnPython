#This is a simple guessing game
import random
import sys
print("Hello!")
print()
#This used to count the total guess
count =0
#This is used to count the positve ansers
positive =0
while(True):
    guess = int(input("Enter a number"))
    num = random.randint(1,9)
    if(guess==num):
        print("Great The guess is right!")
        positive +=1
    elif(guess>num):
        print("The guess is too high!")
    else:
        print("The guess is too low!")
    count +=1
    num=int(input("Enter 1 to continue"))
    if(num!=1):
        print("Thanks for playing The total games were {} \nThe total correct answers were {}".format(count,positive))
        sys.exit()
