"""
11111
2222
333
44
5

Write a program to disply this pattern.

"""

for i in range(1,6): # rows
    for j in range(6,i,-1): # coloms
        print(i,end=" ")
    print()