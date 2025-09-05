# Write a program to find number of vowels in a string.

a = input("Enter here : ")

vowels = 0

for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels +=1
print("NO of vowels is : ", vowels)