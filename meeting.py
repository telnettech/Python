attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently.")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: " + to_line)
print("Cc: " + cc_line)

# List Code Challenge using index to only print continents
# that start with the letter A

continents = [
    'Asia',
    'South America',
    'North America',
    'Africa',
    'Europe',
    'Antarctica',
    'Australia',
]
# Your code here
for continent in continents:
    if continent[0] == "A":
        print("* " + continent)
