
# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

# Start with your program from Exercise 3-6. 
# Add a new line that prints a message saying that you can invite only two people for dinner.

# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# Print a message to each of the two people still on your list, letting them know they’re still invited.

# Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

# Original guest list
guest_list = ["Holly", "Emily", "Katie", "Ashaiya", "Ariely"]
print(guest_list)

# Informing guests about the new dinner table size
print("Due to unforeseen circumstances, we can only invite two guests for dinner.")

print("-" * 25)

# Use pop() to remove guests one by one until only two names remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, we won't be able to invite you to dinner.")

print("-" * 25)

# Print a message to the two remaining guests
for remaining_guest in guest_list:
    print(f"{remaining_guest}, you're still invited to dinner!")

print("-" * 25)

# Use del to remove the last two names from the list
del guest_list[-2:]

# Print to verify the list is empty
print(guest_list)
