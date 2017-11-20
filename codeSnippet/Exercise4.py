x = 2
print(x == 2)
print(x != 2)
print(x > 2)
print(x < 2)
print(x >= 2)
print(x <= 2)

name = "Bernard"
age = 20
if name == "Bernard" and age == 20:
    print("My name is Bernard")

if name == "Bernard" or name == "John":
    print("My name is either Bernard or John")

list = ["Bernard", "John", "Kelly"]
if name in list:
    print("%s is in the list" % name)

if x == 2:
    print("x equals two!")
else:
    print("x not equals two!")

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

print(not False)
print((not False) == (False))