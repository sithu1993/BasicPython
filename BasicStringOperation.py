"""

You will learn basic string operation.

"""

# string length
myString = "Hello, World!"
print(len(myString))

# string output by index
myString = "Hello, World!"
print(myString.index("o"))

# string count
myString = "Hello, World"
print(myString.count("o"))

# string output by slice [start,stop]
myString = "Hello, World"
print(myString[2:8])

# string output by slice with skip [start,stop,step]
myString = "Hello, World"
print(myString[2:8])
print(myString[2:8:2])

# reverse string
myString = "Hello, World!"
print(myString[::-1])

# upper and lower case in string
myString = "Hello, World!"
print(myString.lower())
print(myString.upper())

# check word in string start and end and it is case sensitive
myString = "Hello, World!"
print(myString.startswith("Hello"))
print(myString.endswith("Global"))

# splitting the string into the list
myString = "Hello, World!"
print(myString.split(" "))
