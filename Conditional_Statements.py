"""
Conditional Statement

Conditional statement allow computer to execute a certain condition only if it is true.


Types :
- If the Statement
- If-else Statement
- If-elif-else Statement
- Nested Statement
- Short Hand If Statement
 
"""
"""
1) - If Statement :
     The if statement is the most fundamental decision0making statement 
     The if statement in python has the subsequent syntax:
     if expression 
     statement
"""

marks = int(input("Enter Your Marks : "))

if marks >= 90:
    print("Your will get a Mobile..")

print("Thank You.")

"""
2) - If-Else Statement
     If-else statement is used when you want to give two conditions to the computer.
     Here if one condition is false, program executes the another condition.

     if condition:
      # will executes this block if the condition id true
     else:
      # will executes this block if the condition is false

"""

age = int(input("Enter your age : "))

if age >= 18:
    print("Your Eligible to vote...")
else:
    print("Your not Eligible to vote..")

print("Thanks.....")

"""
3) - if-elif-else Statement :
     In this case, the if condition is evaluated first. if it is false, the elif statement will be executed, if it also 
     comes false then else statement will be executed.
     for multiple conditions, more elif statements are added.

     if condition:
        Body of if
     elif condition:
        Body of elif
     else:
        Body of else

"""

marks = int(input("Enter Your Marks : "))

if marks >= 90:
    print("Gread A")
elif marks >= 80 and marks<= 90:
    print("Gread B")
elif marks >= 70 and marks<= 80:
    print("Gread C")
elif marks >= 60 and marks<= 70:
    print("Gread D")
elif marks >= 50 and marks<= 60:
    print("Gread E")
else:
    print("Fail")

print("Thank you...")



"""
4) - Nested If Statement 
     A nested if statement is one in which an if statement is nestled inside another if statement.
     This is used when a variable must be processed more than once.
     The nested if statement in pyhon has the following syntax:

     if(Condition1):
      # Executes if condition 1 is true
      if(condition 2):
       # Exxecutes if condition 2 is true
       # condition 2 ends here
      # condition  1 ends here 
"""

marks = int(input("Enter your marks : "))

if(marks >= 80):
    print("You got Gread A.")
    if marks>=95:
        print("You got Mobile..")
else:
    print("Ur Fail")


"""
5) - Shot hand if Statement 
     Shor hand if statement is used when only one statement needs to be executed inside the if block.
     This statement can be mentioned in the same line which holds the if statement.
     The short hand if statement in python has the following syntax:
     if condition : satement

"""
marks = int(input("Enter your marks : "))

if(marks >= 80): print("You got Gread A.")
   

"""
6) - shor hand if-else Statement

     It is used to menition if-else statements in one line in which thereis only one statement to exexute in both if and else blocks.
     in simple word if you have only one statement to execute, one for if, and one for else, you can put it all on the same line

      
"""

marks = int(input("Enter your marks : "))
print("You got Gread A.") if(marks >= 80) else print("No Phone")
