
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.

# Start with your program from Exercise 3-4. 
# Add a print() call at the end of your program, stating the name of the guest who can’t make it.

#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

#Print a second set of invitation messages, one for each person who is still in your list.

# Original guest list
guest_list = ["Holly", "Derek", "Katie"]
print(guest_list)

# Removes Derek from party
del guest_list[1]

# List to store invited guests
invited = []
print(invited)

print("-" * 25)

# Send out invitations
while guest_list:
    name = guest_list.pop()
    invited.append(name)

# Not being able to make it
guest_not_attending = "Derek"
print(f"Unfortunately, {guest_not_attending} can't make it to dinner.")

# Replace the guest who can't make it with a new guest
new_guest = "Emily"
guest_list.append(new_guest)

print(f"{guest_not_attending} is replaced with {new_guest}.")

# Send out invitations again
while guest_list:
    name = guest_list.pop()
    invited.append(name)

print("-" * 25)

print(guest_list)
print(invited)
