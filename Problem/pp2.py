"""
1
22
333
4444
55555

Write a program to create this.

"""

for i in range(1,6): # rows
    for j in range(1,i+1): # coloms
        print(i,end=" ")
    print()