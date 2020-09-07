name = input("Please enter your name: ")
number = input("Please enter a number: ")

# TODO: Make sure the number is an integer
number = int(number)

# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
print("Hey {}: \nThe number {}...".format(name, number))

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions.
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************


# TODO: Define variables for is_fizz and is_buzz that stores
# a Boolean value of the condition. Remember that the modulo operator, %,
# can be used to check if there is a remainder.
is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

# Using the variables, check condition of value, and print the necessary
# string
if is_fizz and is_buzz:
    print("is a fizzbuzz number.")
elif is_fizz:
    print("is a Fizz number.")
elif is_buzz:
    print("is a Buzz number.")
else:
    print("is neither a fizzy or buzzy number.")

# Step 1
# Ask the user for their name and the year they were born.
name = input("What should i call you? ")

while True:
    birth_year = input("What year were you born? ")
    try:
        birth_year = int(birth_year)
    except ValueError:
        continue
    else:
        break

# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
current_year = 2020
current_age = current_year - birth_year
turn_25 = (25 - current_age) + current_year
turn_50 = (50 - current_age) + current_year
turn_75 = (75 - current_age) + current_year
turn_100 = (100 - current_age) + current_year

# Step 3
# If they're already past any of these ages, skip them.
if turn_25 > current_year:
    print("You will turn 25 in the year {}, {}".format(turn_25, name))
if turn_50 > current_year:
    print("You will turn 50 in the year {}, {}".format(turn_50, name))
if turn_75 > current_year:
    print("You will turn 75 in the year {}, {}".format(turn_75, name))
if turn_100 > current_year:
    print("You will turn 100 in the year {}, {}".format(turn_100, name))
