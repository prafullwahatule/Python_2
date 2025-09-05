# Function are a set of code, which once created, they can be used throughout the program.

# Function help break our program into smaller parts and helps it look more organized and manageabke.
"""
def Hello():
    print("Hello world")

Hello()

def add():
    a = 20
    b = 45
    print(a+b)

add()
"""

# Parameters and Arguments

"""
Parameters : Parameters are the variables wirtten inside the parentheses with the name of function.function

Argument : Arguments are the value passed to the parameters while challi function.



def add(a,b):
    print(a+b)

add(50,45)
add(6,5)

#******************************************************

def rect (length, width):
    print("The area of rectangle is : ",length*width)

rect(10,52)

"""

# Return Statement and Recursion in python

"""
Return Statement
     Return keyword in python is used t o exit a function and return the value if the function

def hello():
    return("Hello World")

print(hello())

def add (a,v):
    return("The addition of two num : ",a+v)
print(add(10,20))

"""

""""
Recursion in Python
     Recursion in most commonly used mathematucal and programming concept.
     In simple words, recursion means a function can call itself, giving us a benefit of
     loopint throuht data in order to get a result.


def hello():
    return hello()

print(hello())


def fact (n):
    if n == 1:
        return 1
    else:
        return(n*fact(n-1))
    
print(fact(5))


"""
# Advantages and disadvantagess of recursion
"""
ADV: 
     They make the code look clean and organized.
     By the use of recursive functions, a complex task can be brroken down into small sub - parts.
     Sequence generation becomes easier.
DIS ADV:
     Recursive function stake up a lot of memory.
     Sometimes the logic becomes hard to follow.
     There are harde to debugging code of recursion
    
"""