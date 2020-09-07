

first_name = input("What is your name? ")

# Using  if and else statements
if first_name == "Brian":
    print(first_name, "is learning Python")
elif first_name == "Julie":
    print(first_name, "is learning with fellow students in community! Me too!")
else:
    # This is how to add a statement in Python
    age = int(input("How old are you? "))
    if age <= 6:
        print("WOW!! You are {}! If you're confident with reading already...".format(age))
    else:
        print("You should totally learn Python, {}".format(first_name))
print("Have a nice day {}!".format(first_name))


# Creating functions to be used within your code

def yell(text):  # the function is called yell
    text = text.upper()
    num_of_chars = len(text)
    result = text + "!" * (num_of_chars // 2)
    print(result)


# This part of code is calling the yell function that was created
yell("You are doing great")
yell("Dont forget to ask for help")
yell("Dont Repeat Yourself. Keep thing DRY")
