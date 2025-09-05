# Create a program to create are calculator

print("Area Calculator")
print("""Prass 1 to Get the are of Squre...
      Press 2 to get the area of reactangle
      Press 3 t0 get the area of circle
      Press 4 to get are of traingle""")

choice = int (input("Enter a number between 1-4 : "))

if choice == 1:
    side = float(input("Enter the lenght of one side :" ))
    area = side ** 2
    print(area)
elif choice == 2 :
    lenght = float(input("Enter the lenght of the rectangle : "))
    width = float(input("Enter the width of rectangle : "))
    area = lenght*width
    print(area)

elif choice ==3 :
    radius = float(input("Enter the radius of the circle :"))
    area = radius*3.14
    print(area)

elif choice == 4:
    base = float(input('Enter the base of trangle :'))
    hight = float(input('Enter the hight of trangle :'))
    area = 0.5*base*hight
    print(area)

else:
    print("invalid input..")