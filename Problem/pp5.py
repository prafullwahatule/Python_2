"""
1
21
321
4321
54321

write a program to display this pattern.

"""

for i in range(1,6):
    for j in range(1, i +1):
        print("*",end = "  ")
    print()
for i in range(0,0,-1):
    for k in range(1,i-1):
        print(k,end=" ")
    print()
