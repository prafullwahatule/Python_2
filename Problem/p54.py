# Write a function to find maximum of three numbers in python
def maximum_num(a,b,c):
    if a>b or a>c:
        print("Value",a,"is maximum.")
    elif b>a or b>c:
        print("Value",b,"is maximum.")
    else:
        print("Value",c,"is maximum.")

maximum_num(10,20,12)
