# Write a python script to print a dictionary where th ekeys are numbers between 1 to 15 and the values are square of keys.


dic = {}
for i in range(1,16):
    dic[i] = i**2
print(dic)