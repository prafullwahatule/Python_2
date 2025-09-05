# Type Casting
 
# Conversion of one datatype to another is called as type-casting

# There are two types of type-casting:
# 1- Implicit Type Conversion : Where python itself converts one datatype to another.
# 2- Exxplicit Type Conversion : Where the user converts one datatype to another.

"""
a = 10
name = "Prafull"
b = 10.12
c = True

print(type(a))
print(type(name))
print(type(b))
print(type(c))

"""
a = 1223
b = 12.12

print(type(a))
print(type(b))
b = int(b)   # b convert into int type

c = a+b
print(c)
print(type(c))