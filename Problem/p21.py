# Write a program to get fibonacci series up to 10 numbers,

a = 0 
b = 1
n  =int(input("Enter No : "))
if n == 1:
    print(1)
else:
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)