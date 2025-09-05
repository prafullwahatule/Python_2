# Write a program to create  a billing system at supermarket.

print("Welcome to KJ's Super Market...\nPlease Select Your Product for Billing.....")


while True:
    name = input("Enter Your Name : ")
    total = 0

    while True:
        print("Enter the Amount and Quantity : ")
        amount = float(input("Enter amount : "))
        Quantity = float(input("Enter Quantity : "))
        total += amount*Quantity
        repeat = input("Do you want add more item ? (yes/no) : ")
        if repeat == "no" or repeat == "No":
            break
    print("_"*40)
    print("Name :",name)
    print("Amount to be Paid : ",total)
    print("_"*40)
    print("**********Happy Shopping************")

    repeat1 = input("Do you want to go to next Coustomer? (yes/no): ")

    if repeat == "no" or repeat == "No":
        break
