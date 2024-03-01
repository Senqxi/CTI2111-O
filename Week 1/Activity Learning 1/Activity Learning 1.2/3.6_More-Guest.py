
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

#Start with your program from Exercise 3-4 or 3-5. 
# Add a print() call to the end of your program, informing people that you found a bigger table.

#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.

#Print a new set of invitation messages, one for each person in your list.

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

# Informing about the bigger table
print("Good news! We found a bigger dinner table.")

# Adding three more guests
guest_list.insert(0, "Ashaiya")  # Add one new guest to the beginning of the list
guest_list.insert(len(guest_list) // 2, "Kylee")  # Add one new guest to the middle of the list
guest_list.append("Ariely")  # Add one new guest to the end of the list

# Send out invitations for the new guests
for guest in guest_list:
    invited.append(guest)
    print(f"{guest}, you have been invited to dinner!")

print("-" * 25)

print(invited)
