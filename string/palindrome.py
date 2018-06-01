#ask user for an input
string = input("Enter a string : ")
if(string != "" and string[::]==string[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
