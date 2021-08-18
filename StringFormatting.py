"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)

"""
# usage of %s
formatString = "World"
print("Hello, %s" % formatString)

# usage of %s and %d
name = "John"
age = 27
print("%s is %d " % (name, age))

name = ["John", "Mike", 24, 34]
print("%s" % name)

