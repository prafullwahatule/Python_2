# Write a  program to multiply all the items in a dictionary


dic = {"a":1,"h":2,"g":3,"w":4,"r":5,"e":6,"s":7,}

product = 1
for i in dic:
    product *= dic[i]

print(product)