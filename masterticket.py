SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100


def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1:

    print("There are {} tickets reamining".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("How many tickets would you like? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no. We ran into an issue. {} Please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        should_proceed = input("Do you want to proceed? Y/N ")
        if should_proceed.lower() == "y":
            # TODO: Gather CC information and process it
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}".format(name))
print("Sorry. There are no tickets left :( {}".format(name))


# That's Odd Challende

def is_odd(num):
    return(num % 2)


# Use an External Function

from twitter import (
    tweet,
    MessageTooLongError,
    CommunicationError,
)


message = input("What would you like to tweet?  ")
# Your code here

try:
    tweet(message)
except CommunicationError:
    print("An error occurred attempting to connect to Twitter. Please try again!")

except MessageTooLongError as err:
    print("Oh no! Your message was too long {}".format(err))