# Functions
def my_function():
    print("Hello from my_function()!")


my_function()


def my_function_with_args(username, greeting):
    print("Hello %s, I wish you %s in my_function_with_args()!"%(username, greeting))


my_function_with_args("John", "happy new year")


def sum_two_numbers(num1, num2):
    return num1 + num2


print(sum_two_numbers(5, 7))
