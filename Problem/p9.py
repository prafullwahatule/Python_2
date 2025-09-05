#Werite a  program check whether the passed letteris a vowel or not.

letter = input("Enter the Letter of Check it is vovel or not : ")
# aeiou
if (letter in "aeiou") or (letter in "AEIOU"):
    print("It is Vowel")
else:
    print("It is not Vowel")