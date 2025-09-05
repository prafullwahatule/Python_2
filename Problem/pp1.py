"""
1
12
123
1234
12345

write a program to display this pattern.
"""

for i in range(1,6): # rows
    for j in range(1,i+1): # coloms
        print(j,end=" ")
    print()

for i in range(1,6): # rows
    for j in range(1,i+1): # coloms
        print("*",end=" ")
    print()