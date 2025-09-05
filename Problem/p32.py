# Write a program to check if a string is palindrome.
a = input("Enter Here : ")

rev = a[::-1]

if a == rev:
    print("It is Palindrom")
else:
    print("It is not Palindrom")