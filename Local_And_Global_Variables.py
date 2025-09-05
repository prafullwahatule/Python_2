"""
Local Variables:
     Local variables are restricted to only one block of code and cannot be changed throughtout the program.

Global Variables:
     Globle variables are not restricted to one block of code and the can be changed througout the program.
"""
x = 24
def hello ():
    x = 25
    return x
print(hello())

x = 24
def hello ():
    global x
    x = 25
    return x
print(hello())