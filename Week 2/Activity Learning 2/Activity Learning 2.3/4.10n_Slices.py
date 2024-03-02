
# The following example involves a list of players on a team:

'''
players.py

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
'''

# This code prints a slice of the list. 
# The output retains the structure of the list, and includes the first three players in the list:

'''
['charles', 'martina', 'michael']
'''

# You can generate any subset of a list. 
# For example, if you want the second, third, and fourth items in a list, 
# you would start the slice at index 1 and end it at index 4:

'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
'''

# This time the slice starts with 'martina' and ends with 'florence':

'''
['martina', 'michael', 'florence']
'''

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:

'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
'''

# Without a starting index, Python starts at the beginning of the list:

'''
['charles', 'martina', 'michael', 'florence']
'''

# A similar syntax works if you want a slice that includes the end of a list. For example, 
# if you want all items from the third item through the last item, 
# you can start with index 2 and omit the second index:

'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
'''

# Python returns all items from the third item through the end of the list:

'''
['michael', 'florence', 'eli']
'''

# This syntax allows you to output all of the elements from any point in your list to the end, 
# regardless of the length of the list. 
# Recall that a negative index returns an element a certain distance from the end of a list; 
# therefore, you can output any slice from the end of a list. 
# For example, if we want to output the last three players on the roster, we can use the slice players[-3:]:

'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
'''

# This prints the names of the last three players and will continue to work as the list of players changes in size.

'''
['michael', 'florence', 'eli']
'''

##############################################################################################################

################ Looping Through a Slice ####################

# You can use a slice in a for loop if you want to loop through a subset of the elements in a list. 
# In the next example, we loop through the first three players and print their names as part of a simple roster:

'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
❶ for player in players[:3]:
    print(player.title())
'''

# Instead of looping through the entire list of players, Python loops through only the first three names ❶:

'''
Here are the first three players on my team:
Charles
Martina
Michael
'''

# Slices are very useful in a number of situations. 
# For instance, when you’re creating a game, you could add a player’s final score to a list every time that player finishes playing. 
# You could then get a player’s top three scores by sorting the list in decreasing order and taking a slice that includes just the first three scores. 
# When you’re working with data, you can use slices to process your data in chunks of a specific size. Or, 
# when you’re building a web application, you could use slices to display information in a series of pages with an appropriate amount of information on each page.

############# Copying a List ################

# Often, you’ll want to start with an existing list and make an entirely new list based on the first one. 
# Let’s explore how copying a list works and examine one situation in which copying a list is useful.

# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). 
# This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

# For example, imagine we have a list of our favorite foods and want to make a separate list of foods that a friend likes. 
# This friend likes everything in our list so far, so we can create their list by copying ours:

'''
foods.py

my_foods = ['pizza', 'falafel', 'carrot cake']
❶ friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
'''

# First, we make a list of the foods we like called my_foods. 
# Then we make a new list called friend_foods. 
# We make a copy of my_foods by asking for a slice of my_foods without specifying any indices ❶, and assign the copy to friend_foods. 
# When we print each list, we see that they both contain the same foods:

'''
My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
'''

# To prove that we actually have two separate lists, we’ll add a new food to each list and show that each list keeps track of the appropriate person’s favorite foods:

'''
my_foods = ['pizza', 'falafel', 'carrot cake']
❶ friend_foods = my_foods[:]

❷ my_foods.append('cannoli')
❸ friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
'''

# We copy the original items in my_foods to the new list friend_foods, as we did in the previous example ❶.
# Next, we add a new food to each list: we add 'cannoli' to my_foods ❷, and we add 'ice cream' to friend_foods ❸.
# We then print the two lists to see whether each of these foods is in the appropriate list:

'''
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
'''

# The output shows that 'cannoli' now appears in our list of favorite foods but 'ice cream' does not.
# We can see that 'ice cream' now appears in our friend’s list but 'cannoli' does not.
# If we had simply set friend_foods equal to my_foods, we would not produce two separate lists. 
# For example, here’s what happens when you try to copy a list without using a slice:

'''
my_foods = ['pizza', 'falafel', 'carrot cake']

#### This doesn't work: ####
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
'''

# Instead of assigning a copy of my_foods to friend_foods, we set friend_foods equal to my_foods.
# This syntax actually tells Python to associate the new variable friend_foods with the list that is already associated with my_foods,
# so now both variables point to the same list. 
# As a result, when we add 'cannoli' to my_foods, it will also appear in friend_foods.
# Likewise 'ice cream' will appear in both lists, even though it appears to be added only to friend_foods.

# The output shows that both lists are the same now, which is NOT what we wanted:

'''
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
'''

####################################################################################################################

#4-10. Slices: 
# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

# Print the message The first three items in the list are:. 
# Then use a slice to print the first three items from that program’s list.

# Print the message Three items from the middle of the list are:. 
# Then use a slice to print three items from the middle of the list.

# Print the message The last three items in the list are:. 
# Then use a slice to print the last three items in the list.

import os 

os.system('Clear')
print("-"*37)

Pizzas = ["Chicken", "Bacon Ranch", "Meat Lovers", "Hawaiian", "Pepperoni", "Cheese"]
print(Pizzas[:-3])
print(Pizzas[1:4])
print(Pizzas[-3:])
