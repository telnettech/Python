
num = 10


def print_fav_movie():
    print('Full Metal Jacket')


def set_num():
    num = 5
    print(num)


# Getting value out of a function
def two_plus_two():
    val = 2 + 2
    return val


# Passing Argument to Function
def add_two(num):
    val = num + 2
    return val


def multi_param(num1, num2):
    val = num1 + num2
    return val


# Packing a Function
def packer(*args):
    print(args)


# Packing a function with a for loop
def packer_loop(*args):
    for val in args:
        print(val)


def calculate_total(*args):
    total = sum(args)
    print(total)


# Using function to unpack variables
def unpacker():
    return (1, 2, 3)


def unpacker2():
    return 'hey'


print_fav_movie()
set_num()
print(two_plus_two())
value = two_plus_two()
print(value)
print(two_plus_two() * 2)
add_two(5)
print(add_two(5))  # Parameter 'num' from function needed within print statement
print(multi_param(5, 10))  # Both parameters needed for function to work.
packer('hi', 'I', 'love', 'python')
packer_loop('hi', 'I', 'love', 'python')  # Prints on individual lines
calculate_total(25, 25, 20, 30)
var1, var2, var3 = unpacker()  # Takes function and puts values to variables
print(var1)
print(var2)
print(var3)
var1, var2, var3 = unpacker2()
print(var1)
print(var2)
print(var3)
