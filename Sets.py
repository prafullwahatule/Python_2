"""
Sets 
     Sets are unordered collection of data. Every element inside the set is unique and mutable.
        - Sets are wirtten inside the curly brackets.
        - The value inside a set is separated by coma(,)
        - Mutable means once created, they can be changed.

"""

# a = {"Prafull","Wahatule","Piyush","Shinde","Vedant"}
# print(a)
# print(type(a))

# for x in a:
#     print(x)

# *************************************

# Set Function 1
"""
a = {"Prafull","Wahatule","Piyush","Shinde","Sakshi"}

#add
a.add("Harshi")
print(a)

# pop
a.pop()
print(a)

# remove
a.remove("Sakshi")
print(a)

# discard
a.discard("Wahatule")
print(a)

# copy
b = a.copy()
print(b)

"""


# Set Function 2
"""
a = {"Prafull","Wahatule","Hulk","Thor","Piyush","Shinde","Sakshi"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor"} 

# isdisjoint
print(a.isdisjoint(c))

# issubset
print(c.issubset(a))

# issuperset
print(a.issuperset(c))

# update
a.update(b)
print(a)

# clear
a.clear()
print(a)

"""

# Set Function 3
a = {"Prafull","Wahatule","Hulk","Thor","Piyush","Shinde","Sakshi"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor"} 

# union 
print(a.union(b))

# Difference
print(a.difference(c))

# Difference update
print(a.difference_update(c))

# Intersection
print(c.intersection(a))

# Intersection Update
print(b.intersection_update(c))

# Symmetric Difference
print(a.symmetric_difference(c))

# Symmetric difference update
print(a.symmetric_difference_update(b))