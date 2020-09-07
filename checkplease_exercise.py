# This includes the math method built in Python library to be used by code

import math

# This is the a function that is designed by me


def split_check(total, num_people):
    if num_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / num_people)


try:
    total_due = float(input("What is the total? "))
    num_people = int(input("How many people? "))
    amount_due = split_check(total_due, num_people)
except ValueError as err:
    print("Oh no! Try again please....")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))
