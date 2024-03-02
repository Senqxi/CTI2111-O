
# 4-2. Animals: 
# Think of at least three different animals that have a common characteristic. 
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

# Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program, stating what these animals have in common. 
# You could print a sentence, such as Any of these animals would make a great pet!

import os 

os.system('Clear')
print("-"*37)

Pets = ["Lizard", "Snake", "Gecko"]

for Pet in Pets:
    print(f"I would love to have a {Pet} as a pet.")

print(f"They are all cold-blooded animals that can be pets")