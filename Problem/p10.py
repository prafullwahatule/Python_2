# Write a program to check if a number is  a single digit number , or 2- digit number and so on.. up to 5 digits.

num = float(input("Enter the Number : "))

if num >= 0 and num <=9:
    print("It's Single digit number..")

elif num >= 10 and num <=99:
    print("It's Two digit number..")


elif num >= 100 and num <=999:
    print("It's Three digit number..")


elif num >= 1000 and num <=9999:
    print("It's Four digit number..")


elif num >= 10000 and num <=99999:
    print("It's Five digit number..")

else:
    print("It's Number is More than Five Digits... \nThank You.......")