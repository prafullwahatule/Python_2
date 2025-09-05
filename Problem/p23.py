# write a program to check no is palindrom or not.

num = int (input("Enter number : "))
temp = num
rev = 0
while num > 0:
    dig = num %10
    rev = rev * 10 + dig
    num = num // 10
if rev == temp:
    print("It is palindrome")
else:
    print("it is not palindrome")