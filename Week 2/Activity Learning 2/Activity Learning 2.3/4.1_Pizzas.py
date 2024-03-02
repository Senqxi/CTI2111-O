
# Say we have a list of magicians’ names, and we want to print out each name in the list. 
# We could do this by retrieving each name from the list individually, but this approach could cause several problems. 
# For one, it would be repetitive to do this with a long list of names. Also, we’d have to change our code each time the list’s length changed. 
# Using a for loop avoids both of these issues by letting Python manage these issues internally.


# When you want to do the same action with every item in a list, you can use Python’s for loop.
'''
magicians.py

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

alice
david
carolina
'''

# You can also write as many lines of code as you like in the for loop. 
# Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list. 
# Therefore, you can do as much work as you like with each value in the list.

# What happens once a for loop has finished executing? 
# Usually, you’ll want to summarize a block of output or move on to other work that your program must accomplish.

# Any lines of code after the for loop that are not indented are executed once without repetition.
'''
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
'''

##############  #############################  #############################  #############################  #############################  ###############

# 4-1. Pizzas: 
# Think of at least three kinds of your favorite pizza. 
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.

# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.

# Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

import os 

os.system('Clear')
print("-"*37)

Pizzas = ["Chicken Bacon Ranch", "Meat Lovers", "Hawaiian"]

for Pizza in Pizzas:
    print(f"I love {Pizza.title()} pizza.")

print("I can eat pizza for the rest of my life.\n")