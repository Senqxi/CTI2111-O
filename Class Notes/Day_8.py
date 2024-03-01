# # David's Marble Collection
# #--------------------------

# '''
# red: 2
# orange: 1
# purple: 3
# yellow: 2
# green: 2
# blue: 0      <—--- David Sad
# white: 1
# swirl: 2
# '''

# # Difficult for David to find blue marbles. One day he visits a hobby shop that sells marbles. There is a secret bag inside the store. Each day, children
# # may pull up to 5 marbles(one at a time) from the bag in the hopes of finding the color marble they seek. In David's case, 
# # this is a blue marble. Any marble that isn't kept must be returned to the bag. If David locates a blue marble, 
# # that will be the last selection and he will stop choosing marbles.

# # Secret Bag Inventory
# #---------------------

# '''
# blue: 3
# green: 2
# orange: 2
# purple: 3
# yellow: 2
# pink: 2
# red: 5
# '''

# # Create a program that tracks how many times David picks a marble from the secret bag and confirm whether the marble chosen is blue. If blue is picked,
# # add that blue marble to David's collection. We also want to remove that blue marble from the secret bag's inventory. Remember you only have 5 chances per day

# Begin Program
#-------------
import random 
import time
import os

# David's Marble Collection
marble_collection = ['red', 'orange','red','green', 'green', 'swirl', 'white', 'yellow', 'orange', 'purple', 'yellow', 'swirl', 'purple', 'purple']

# Secret Bag Inventory

# Secret Bag Inventory
secret_bag = ['blue','blue','blue','green','green','orange','orange','red','red','red','red','swirl','swirl','white','purple','purple','purple','yellow', 'yellow', 'pink', 'pink', 'red',]

# Marbles Chosen
marbles_chosen = []

# Daily attempts
tries_available = 5

y = 'Yes'
n = 'No'

while Game_Start == 'Yes':
    Game_Start = print(input('Are you ready to pick your marBALLLS!!!? [y or n]: '))
    time.sleep(2)
    os.system('clear')



while tries_available > 0:
    selected_marble = print(random.choice(secret_bag))
    if selected_marble == "blue":
        print('You have gotten your favorite marble!')
        secret_bag.remove(selected_marble)
        break
    else:
        marbles_chosen.append(selected_marble)
        tries_available -= 1