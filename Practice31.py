# Write a recurcive function to calculate the sum of first n natural numbers.

def calc_sum(n):
    if(n ==0):
        return 0
    print(n)
    return calc_sum(n-1) + n
sum = calc_sum(10)
print(sum)