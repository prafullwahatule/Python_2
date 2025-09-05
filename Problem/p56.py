# Write a python function that takes a number as a parameter and check if the number is prime or not.

def check_prime(num):
    if num == 1:
        print("It is not prime number.")
    if num == 2:
        print("It is not prime number")
    if num > 2:
        for i in range(2,num):
            if num % i == 0:
                print("It is not a prime Number...")
                break
            else:
                print("It is Prime Number...")
                break
check_prime(31)

