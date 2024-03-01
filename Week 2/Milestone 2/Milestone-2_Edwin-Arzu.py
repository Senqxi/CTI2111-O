

# [Edwin Arzu]
# [Sun Feb 18th, 2024]
# [Python 3.11]
# [Milestone 2 - Fight Club: The 1st Rule is...]

###### Import the random Module #####

import random
import time
import os

###### Here are your list of Fighters #####
fighters = [
    'Vegeta',
    'Goku',
    'Krillin',
    'Piccolo',
    'Trunks',
    'Broly',
    'Gohan',
    'Android 17',
    'Android 18',
    'Cell',
    'Frieza',
    'Majin Buu',
    'Dabura'
]

#####  Attacks List #####
attacks = ['kick' ,'throw' ,'punch']
defense = ['blocking', 'instant_t']

# I needed to represent what attack beats the other in condition
attack_relations = [
    ('punch' , 'throw'),
    ('throw' , 'kick'),
    ('kick' , 'punch'),
    ('throw' , 'punch'),
    ('kick' , 'throw'),
    ('punch' , 'kick')
]

##### Choosing the Characters for the fight #####
player = random.choice(fighters)
opponent = random.choice(fighters)

character = [
    ('player', player),
    ('opponent', opponent)
]

##### Announce Game Start #####
print("-" * 50)
print("Welcome to the fight club! The battle awaits!")
print("-" * 50)
print(f"{player} has challenged {opponent} in one on one combat!")
time.sleep(3)
os.system('clear')

##### Initialize Scoring Variables ##### 
pscore = 0
oscore = 0

while pscore < 5 and oscore <5:
    print(f'Current score   {player}: {pscore}     {opponent}: {oscore} ')
    print("-" * 50)
    time.sleep(.7)
    
    random.shuffle(attacks)
    random.shuffle(attacks)
    
    pattack = random.choice(attacks)
    oattack = random.choice(attacks)
    
    pdefense = random.choice(defense)
    odefense = random.choice(defense)
    
    if pattack == oattack:
        print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')
        time.sleep(.7)
        print('It\'s a Tie!!')
        
    else:
        for attack_pair in attack_relations:
            if (pattack, oattack) == attack_pair:
                print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')
                time.sleep(.7)
                #os.system('clear')
                print(f'{player} WINS ROUND!')
                pscore += 1
                break
            elif (oattack, pattack) == attack_pair:
                print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')
                time.sleep(.7)
                #os.system('clear')
                print(f'{opponent} WINS ROUND!')
                oscore += 1
                break
print("-" * 50)
winner = [f'{player}' if pscore == 5 else f'{opponent}']
print(f'Final score is {pscore} - {oscore} the winner is {winner}')
# time.sleep(20)
# os.system('clear')

# Create a loop that will run UNTIL either the player or opponent scores 5 points
# Write your code below this row 👇

# This code needs to be nested inside your loop 👇
# THINK: Recall that any code nested inside a loop will run each time the loop executes
##### Choosing the attack #####

# Create a scoring system to record 1 point for each 'win' scored by either the player or the opponent
# HINT: You will need to use conditionals to compare the attacks
# HINT: You will need to update the score variables 
# Write your code below this row 👇

# Punch > Throw      
# Throw > Kicks
# Kicks > Punch

# Create a conditional outside of the loop to print the winner's name.
# Write your code below this row 👇