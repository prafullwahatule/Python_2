"""
Continue statement:
Continue Statement is used when you want to skip a particular condition.
Break Statement:
break Statement is used when you want to destroy a loop at a certain condition ansd come out of the loop.

"""


for i in range(1,11):
    if i == 7:
        continue
    else:
        print(i)


for i in range(1,11):
    if i == 7:
        break
    else:
        print(i)
