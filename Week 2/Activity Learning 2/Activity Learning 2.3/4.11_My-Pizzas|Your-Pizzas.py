
# 4-11. My Pizzas, Your Pizzas: 

# Start with your program from Exercise 4-1 (page 56). 
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. 
# Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.

import os 

os.system('Clear')
print("-"*37)

Pizzas = ["Chicken", "Bacon Ranch", "Meat Lovers", "Hawaiian", "Pepperoni", "Cheese"]

Friend_Pizza = Pizzas[:]

print("My Favorite Pizza are", Pizzas)
print("My Friend Favorite Pizza are", Friend_Pizza)
