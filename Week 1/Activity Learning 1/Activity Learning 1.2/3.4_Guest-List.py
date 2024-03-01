
# The simplest way to add a new element to a list is to append the item to the list. 
# When you append an item to a list, the new element is added to the end of the list.

# You can add a new element at any position in your list by using the insert() method. 
# You do this by specifying the index of the new element and the value of the new item.

# If you know the position of the item you want to remove from a list, you can use the "del" statement

# The pop() method removes the last item in a list, but it lets you work with that item after removing it. 
# The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. 
# In this analogy, the top of a stack corresponds to the end of a list.

# Imagine that the motorcycles in the list are stored in chronological order, according to when we owned them. 
# If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought

# Remember that each time you use pop(), the item you work with is no longer stored in the list.

# If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: 
# when you want to delete an item from a list and not use that item in any way, use the del statement; 
# if you want to use an item as you remove it, use the pop() method.

'''
❶ motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

❷ popped_motorcycle = motorcycles.pop()
❸ print(motorcycles)
❹ print(popped_motorcycle)
'''

# Sometimes you won’t know the position of the value you want to remove from a list. 
# If you only know the value of the item you want to remove, you can use the remove() method.

'''
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

'''
######################### ########################## #########################

# If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

import os 

os.system('Clear')
print("-"*37)

guest_list = ["Holly", "Derek", "Katie"]
print(guest_list)
invited = []
print(invited)

print("-"*25)

invites = len(guest_list)

while len(guest_list) > 0:
    name = guest_list.pop()
    invited.append(name)
    print(f"{name}, You have been invited to dinner!")

print("-"*25)

print(guest_list)
print(invited)
