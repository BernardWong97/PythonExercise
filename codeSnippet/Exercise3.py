name = "Bernard"
age = 20
print("Hello, %s" % name)
print("%s's age is %d years old" % (name, age))

myList = [1, 2, 3]
print("This is a list: %s" % myList)

aString = "Hello World!"
print(len(aString))
print(aString.index("o"))
print(aString.count("l"))
print(aString[3:7])
print(aString[3:7:2])

print(aString[::-1])
print(aString.upper())
print(aString.lower())
print(aString.startswith("Hello"))
print(aString.endswith("asdfasdf"))

aList = aString.split(" ")
print(aList)
