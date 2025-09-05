#Write a program to write first 20 numbers and their squared numbers.


for i in range(1,21):
    sqr = i * i
    print(i, "*",i,"=",sqr)
    i += 1
print("-----------------------------")

for i in range(1,21):
    cube = i * i * i
    print(i, "*",i,"=",cube)
    i += 1