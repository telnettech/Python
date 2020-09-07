
# Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all of the people in BIRTHDAYS
# If they celebrate their birthday, print out
# "Happy Birthday" and their name
print("Celebrations:")

# Solution 1 here
for person in BIRTHDAYS:
    if person[2]:
        print("Happy Birthday, {}".format(person[0]))
print("-"*20)

# Problem 2: Half birthdays
# Loop through all of the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# Print out their name and half birthday
print("Half birthdays:")

# Solution 2 here
for person in BIRTHDAYS:
    name = person[0]
    birthdate = person[1].split('/')
    birthdate[1] = int(birthdate[1]) + 6
    if birthdate[1] > 12:
        birthdate[1] = birthdate[1] - 12
    birthdate[1] = str(birthdate[1])
    print(name, "/".join(birthdate))

print("-"*20)

# Problem 3: Only school year birthdays
# Loop through the people in BIRTHDAYS
# If their birthday is between September (9)
# And June (6), print their name
print("School birthdays:")

# Solution 3 here
for person in BIRTHDAYS:
    name = person[0]
    birthdate = person[1].split('/')
    birthdate[1] = int(birthdate[1])
    if birthdate[1] in range(1, 7) or birthdate[1] in range(9, 13):
        print(name)
print("-"*20)

# Problem 4: Wishing stars
# Loop through BIRTHDAYS
# If the person celebrates their birthday,
# AND their age is 10 or less,
# Print out their name and as many stars as their age
print("Stars:")

# Solution 4 here
for person in BIRTHDAYS:
    name = person[0]
    age = person[-1]
    celebrates = person[-2]

    if celebrates and age <= 10:
        stars = ''
        for star in range(age):
            stars += '*'
        print(name, stars)

print("-"*20)
