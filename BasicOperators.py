""" In this chapter, you will learn some basic operator.
if you don't know about condition statement(if,elif),
you can learn at Conditions.py

arithmeticOperators = " + ", " - ", " * ", " ** ", " / ", " // "
comparisonOperator = " == ", " != ", " > ", " < ", " >= ", " <= "
logicalOperator = " and ", " or ", " not "
membershipOperator = " in ", " not in "

"""

# addition
result = 1 + 5
print(result)

# subtraction
result = 6 - 3
print(result)

# multiplication
result = 5 * 3
print(result)

# exponent
result = 2 ** 2
print(result)
result = 2 ** 3
print(result)

# division
result = 15 / 2
print(result)

# modulus
result = 15 % 2
print(result)

# floor division
result = 15 // 2
print(result)

print("--- End Simple Basic Operators -----")

""" Using Operator in String """

helloWorld = "hello" + " " + "world"
print(helloWorld)

# multiplying strings to form a string with a repeating sequence
helloWorld = "Hello " * 5
print(helloWorld)

print("--- Using Operator in String ---")

""" Using addition Operators with Lists """

male = ['David', 'Jone', 'Philips']
female = ['Rose', 'Emily', 'May']
gender = male + female
print(gender)

print("--- End of using edition operator in lists ---")

# == operator & and,or operator
name = "John"
age = 27
if name == "John" and age == 27:
    print("Your name is john and age is 27")

if name == "John" or name == "Mike":
    print("Your name is either John or Mike")


# in operator
name = "Mike"
if name in ["Mike", "John"]:
    print("You name is either John or Mike")

# is operator
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)


