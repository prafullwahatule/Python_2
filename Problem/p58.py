# Write a python program to solve the fibonacci sequence using recursion.

def fs(num):
    if num == 1:
        return(0)
    elif num == 2:
        return(1)
    else:
        return(fs(num-1)+fs(num-2))
    
print(fs(11))