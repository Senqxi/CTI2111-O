
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), 
# use len() to print a message indicating the number of people you’re inviting to dinner.

import os 

os.system('Clear')
print("-"*37)

# Original guest list
guest_list = ["Holly", "Derek", "Katie"]
print(guest_list)
print("-"*37)

# Removes Derek from party
del guest_list[1]

# List to store invited guests
invited = []

# Send out invitations
while guest_list:
    name = guest_list.pop()
    invited.append(name)

# Not being able to make it
guest_not_attending = "Derek"
print(f"Unfortunately, {guest_not_attending} can't make it to dinner.")
print("-"*37)


# Replace the guest who can't make it with a new guest
new_guest = "Emily"
guest_list.append(new_guest)
print(f"{guest_not_attending} is replaced with {new_guest}.")
print("-"*37)


# Send out invitations again
while guest_list:
    name = guest_list.pop()
    invited.append(name)

# Informing about the bigger table
print("Good news! We found a bigger dinner table.")
print("-"*37)


# Adding three more guests
guest_list.insert(0, "Ashaiya")  # Add one new guest to the beginning of the list
guest_list.insert(len(guest_list) // 2, "Kylee")  # Add one new guest to the middle of the list
guest_list.append("Ariely")  # Add one new guest to the end of the list

# Send out invitations for the new guests
for guest in guest_list:
    invited.append(guest)
    print(f"{guest}, you have been invited to dinner!")
    print("-"*37)

# Print the number of people invited to dinner
print(f"Number of people invited to dinner: {len(invited)}")
print("-"*37)

