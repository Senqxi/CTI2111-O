
# 4-12. More Loops: 
# All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.

# Example 1 

import os 

os.system('Clear')
print("-"*37)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My food")
for food in my_foods:
    print(food.title())

print("-"*37)

print("Friend food")
for foods in friend_foods:
    print(foods.title())

print("-"*37)

