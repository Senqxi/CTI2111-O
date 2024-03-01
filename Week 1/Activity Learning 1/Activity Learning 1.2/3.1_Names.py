

#################### What Is a List? ###################


# A list is a collection of items in a particular order. 
# You can make a list that includes the letters of the alphabet, the digits from 0 to 9, or the names of all the people in your family. 
# You can put anything you want into a list, and the items in your list don’t have to be related in any particular way. 
# Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names.

# In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

#################### Index Positions Start at 0, Not 1 ###################

# Python considers the first item in a list to be at position 0, not position 1. 
# This is true of most programming languages, and the reason has to do with how the list operations are implemented at a lower level. 
# If you’re receiving unexpected results, ask yourself if you’re making a simple but common off-by-one error.

# The second item in a list has an index of 1. 
# Using this counting system, you can get any element you want from a list by subtracting one from its position in the list. 
# For instance, to access the fourth item in a list, you request the item at index 3.

# Python has a special syntax for accessing the last element in a list. 
# If you ask for the item at index -1, Python always returns the last item in the list

################### ################### ################### ###################

# Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

Names = ['Beth', 'Malorie', 'Madison', 'Alex']

print(Names[0])
print(Names[1])
print(Names[2])
print(Names[3])