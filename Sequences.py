groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

for item in groceries:
    print(item)

index = 1
for item in groceries:
    print(f'{index}. {item}')
    index += 1
# OR include enumerate method and use a tuple in the for statement
for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')

# Ranges range(start, stop, step)
for i in range(0, 10, 1):
    print(i)
# OR
for i in range(10):
    print(i)

# Slices variable[start, stop, step]
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(rainbow[1])
print(rainbow[1:4])
print(rainbow[3:])
# The following statement goes thru list and prints every other string
print(rainbow[::2])
# The following statement reverses the sequence
print(rainbow[::-1])

num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(num))
print(max(num))
print(min(num))

my_string = 'treehouse'
print(len(my_string))
print(max(my_string))
print(min(my_string))

mixed = 'treehouse2019'
print(max(mixed))
print(min(mixed))

# Membership Testing. Checks if tuple is in variable
docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'
if 'tuple' in docs:
    print('tuple is here')
else:
    print('tuple is not here')

if 'tuple' not in docs:
    print('tuple is not here')
else:
    print('tuple is here')
print(docs.count('tuple'))
print(docs.index('tuple'))

# Concatenation
obj1 = [1, 2, 3, 4, 5]
obj2 = [6, 7, 8, 9, 10]
object1 = obj1 + obj2
print(object1)

# Multiplication
str = 'python'
print(str*5)
