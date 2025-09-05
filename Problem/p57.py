# Write a python function to sum all the numbers in a list.

def add(num):
    totals = 0
    for i in num:
        totals = totals+i
    return totals
print(add([12,20,30,40,50,60]))


#Solution 2 Uaing recursion

def add (numbers):
    if len(numbers) == 1:
        return(numbers[0])
    else:
       return (numbers[0]+add(numbers[1:]))

print(add([12,20,30,40,50,60]))
