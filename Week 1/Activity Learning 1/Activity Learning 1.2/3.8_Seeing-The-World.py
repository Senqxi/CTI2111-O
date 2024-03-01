
# Python’s sort() method makes it relatively easy to sort a list. 
# Imagine we have a list of cars and want to change the order of the list to store them alphabetically.

# The sort() method changes the order of the list permanently.

# You can also sort this list in reverse-alphabetical order by passing the argument reverse=True to the sort() method. 

'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
'''

# Sorting a List Temporarily with the sorted() Function
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. 
# The sorted() function lets you display your list in a particular order, but doesn’t affect the actual order of the list.

#Let’s try this function on the list of cars.

'''
cars = ['bmw', 'audi', 'toyota', 'subaru']

❶ print("Here is the original list:")
print(cars)

❷ print("\nHere is the sorted list:")
print(sorted(cars))

❸ print("\nHere is the original list again:")
print(cars)
'''

# We first print the list in its original order ❶ and then in alphabetical order ❷. 
# After the list is displayed in the new order. 
# we show that the list is still stored in its original order ❸:

'''
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

❶ Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
'''

# Notice that the list still exists in its original order ❶ after the sorted() function has been used. 
# The sorted() function can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order.

############# Printing a List in Reverse Order #############

# To reverse the original order of a list, you can use the reverse() method. 
# If we originally stored the list of cars in chronological order according to when we owned them, 
# we could easily rearrange the list into reverse-chronological order:

'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
'''

# Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list:

'''
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
'''

# he reverse() method changes the order of a list permanently 
# but you can revert to the original order anytime by applying reverse() to the same list a second time.

################ Finding the Length of a List ###############

#You can quickly find the length of a list by using the len() function. The list in this example has four items, so its length is 4:

'''
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
'''

# You’ll find len() useful when you need to identify the number of aliens that still need to be shot down in a game, 
#   - determine the amount of data you have to manage in a visualization, 
#   - or figure out the number of registered users on a website, among other tasks.

########################################################################################################################################

# Think of at least five places in the world you’d like to visit.

# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed

import os 

os.system('Clear')
print("-"*37)

# Original list of wonders
wonders = ["Mount Everest", "Stonehenge", "Aurora borealis", "Grand Canyon", "Eiffel Tower"]
print("Original List", wonders)
print("-"*37)

# Use sorted() to print the list in reverse-alphabetical order without modifying the original list
print("Sorted in reverse-alphabetical order:", sorted(wonders, reverse=True))
print("-"*37)

# Use reverse() to change the order of the list
wonders.reverse()

# Print the list to show its order has changed
print("Reversed list:", wonders)
print("-"*37)

# Use reverse() again to change the order back to its original order
wonders.reverse()

# Use sort() to change the list to alphabetical order
wonders.sort()

# Print the list to show its order has changed to alphabetical order
print("Sorted in alphabetical order:", wonders)
print("-"*37)

# Use sort() to change the list to reverse-alphabetical order
wonders.sort(reverse=True)

# Print the list to show its order has changed to reverse-alphabetical order
print("Sorted in reverse-alphabetical order:", wonders)
print("-"*37)

