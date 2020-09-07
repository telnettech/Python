import sys

MASTERPASSWORD = 'opensesame'
password = input("Please enter the super secret password: ")
attempt_count = 1
while password != MASTERPASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, please try again: ")
    attempt_count += 1
print("Welcome to secret town")

# For Loops. This will repeat the code for each letter in the variable banner

banner = "Happy Birthday!"
for letter in banner:
    print(letter.upper())
