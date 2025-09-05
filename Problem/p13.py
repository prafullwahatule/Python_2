# Write a program to find sum of first 10 odd numbrers using while loop

n = 1
sum = 0
while n <= 20:
    if n % 2 != 0:
        sum += n
    n += 1
print(sum)