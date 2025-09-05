# Lambda function in Python
"""
It is used when an anonymous function is requred for short period of time. 
It cna take numerios arguments .
It can only have one expression.

"""

a = lambda b : b*5
print(a(4))

x = lambda a,b,c:(a+b)*c
print(x(3,7,2))