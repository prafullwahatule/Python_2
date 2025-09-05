# Write a program to calculate area Calculator.

# Create a program to create are calculator

print("Area Calculator")
while True:
    print("""Prass 1 to Get the are of Squre...
      Press 2 to get the area of reactangle
      Press 3 t0 get the area of circle
      Press 4 to get are of traingle""")

    choice = int (input("Enter a number between 1-4 : "))

    if choice == 1:
        while True:
            side = float(input("Enter the lenght of one side :" ))
            area = side ** 2
            print(area)
            repeat = input("Do you want to try again with square ? ")
            if repeat == "no" or repeat == "No":
                break

    elif choice == 2 :
        while True:
            lenght = float(input("Enter the lenght of the rectangle : "))
            width = float(input("Enter the width of rectangle : "))
            area = lenght*width
            print(area)
            repeat = input("Do you want to try again with rectangle ? ")
            if repeat == "no" or repeat == "No":
                break

    elif choice ==3 :
        while True:
            radius = float(input("Enter the radius of the circle :"))
            area = radius*3.14
            print(area)
            repeat = input("Do you want to try again with Circle ? ")
            if repeat == "no" or repeat == "No":
                break

    elif choice == 4:
        while True:
            base = float(input('Enter the base of trangle :'))
            hight = float(input('Enter the hight of trangle :'))
            area = 0.5*base*hight
            print(area)
            repeat = input("Do you want to try again with Trangle ? ")
            if repeat == "no" or repeat == "No":
                break

    repeat1 = input("do you want to repeat the menu again ? ")
    if repeat1 == "No" or repeat == "no":
        break

    else:
        print("invalid input..")