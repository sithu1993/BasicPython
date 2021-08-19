""" In this chapter, you will learn about loops

    loops = "for", "while"
"""


x = ["apple", "orange", "cherry"]
for y in x:
    print(y)

for a in "apple":
    print(a)

print("---End of simple loops---")

# range(start,end,increment) function usage
for a in range(6):
    print(a)

for a in range(3, 7):
    print(a)

for a in range(1, 10, 2):
    print(a)

# else in for loop
for x in range(5):
    print(x)
else:
    print("Finally Finished!")

# nested loop
color = ["red", "yellow", "green"]
fruits = ["apple", "banana", "lime"]

for c in color:
    for f in fruits:
        print(c, f)

print("--- End for loop ---")

# while loop
count = 0
while count < 5:
    print(count)
    count += 1


print("------------------")


# break and continue keyword usage
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print("------------------")


for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
