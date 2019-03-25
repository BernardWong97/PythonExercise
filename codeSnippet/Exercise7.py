# Classes
class MyClass:
    variable = "test"

    def function(self):
        print("this message is inside MyClass's function()")


# Object
my_object = MyClass()

print(my_object.variable)
my_object.function()

my_object2 = MyClass()

print(my_object2.variable)

my_object2.variable = "changed this object variable"

print(my_object2.variable)
print(my_object.variable)
