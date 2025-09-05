# Write a program to check if a number is prinme or not.

num = int(input("Enter No : "))

if num <= 1:
    print(num, "is not Prime No...")
else:
    for i in range(2,num):
        if num%i == 0:
            print("no is not a prime no.")
            break
    else:
        print("no is prime no...") 