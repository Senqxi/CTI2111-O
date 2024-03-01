




############## Sequence based Structured ############################# Sequence based Structured ############################# Sequence based Structured ###############
# #  -One line sequence
# #  - code is read as its recieved line by line
# # Example of sequence structured lines
# '''
# # Create Shopping List Variables
# shoes_price = 199.99
# chicken_thighs_price = 4.59
# chicken_breasts_price = 9.99
# milk_price = 4.99
# eggs_price = 3.49

# # Prompt the userfor quantities
# shoes = int( input("How many pairs of shoes would you like?\n"))
# chicken_thighs = int( input("How many pairs of chicken thighs would you like?\n"))
# chicken_breasts = int( input("How many pairs of chicken breast would you like?\n"))
# milk = int( input("How many pairs of milk would you like?\n"))
# eggs = int( input("How many pairs of eggs would you like?\n"))

# # # (') can replace (") so that we can use quotations
# # print('In the movie, Arnold said, "I\'ll be back!"')

# # Cost of Items
# cost_of_items = (shoes * shoes_price) + (chicken_breasts * chicken_breasts) + (chicken_thighs * chicken_thighs_price) + (milk * milk_price) + (eggs * eggs_price)
# print (cost_of_items)

# # Tax Rate
# tax_rate = 0.065

# # Calculate Sub-Total
# tax = cost_of_items * tax_rate
# print (tax)

# # Out the Door
# total = tax + cost_of_items
# print (total)

# # Thank Customer
# print(f"Thanks for shopping with us today. Your total amount is ${total:.2f} and we appreciate your business! Have a nice day.")
# '''

############## Decision Structure ############################# Decision Structure ############################# Decision Structure ############################# Decision Structure ###############

# # Example of Decision Based Structures 

# '''

# # # Testing for multiple conditions #

# # traffic_light = input('What color is the light? ')
# # traffic_light = 'yellow'

# # if traffic_light == 'red':
# #     print("Stop.")

# # elif traffic_light == 'Yellow':
# #     print('Slow down.')

# # else:
# # print ("Step on it!")
# '''

# # Using import function (Libraries)

# # import time
# # import random

# # drinks = ['milk', 'juice', 'soda', 'pop', 'water']

# '''
# print (random.choice(drinks))
# time. sleep (1)
# print (random. choice (drinks))
# time. sleep (1)
# print (random. choice (drinks))
# time. sleep (1)
# print (random. choice (drinks))
# time. sleep (1)
# print (random. choice (drinks))
# time. sleep (1)
# print (random. choice (drinks))
# '''

############## Repetition Structure ############################# Repetition Structure ############################# Repetition Structure ###############

# # For loop are COUNT-CONTROLLED repitition Structure
# # Range Function will count the first number up until the number before 
# # Ex. (1, 6) = 1, 2, 3, 4, 5

# # for x in range(5):
# #     time. sleep (.6)
# #     print(random.choice(drinks))

# # #  =

# # for each_number in range(1, 6):
# #     time. sleep (.6)
# #     print(random.choice(drinks))



# # for x in range(1, 11):
# #     time. sleep (.4)
# #     print (x)

# # #  =

# # for x in range(10):
# #     time. sleep (.4)
# #     print (x)

# # The last # is what the range will count by starting from the first number
# # for x in range(2,101, 2):
# #     print (x)


# # #           1       2       3         4
# # colors = ['red', 'blue', 'green', 'yellow']

# # print('The colors in the rainbow are:')
# # # For each 'color' inside the list of 'colors' execute everything below the For Loop along with each item in the list\
# '''
# for color in colors:
#     time. sleep(.5)
#     print(color.upper())
#     print('-' * 25)
# '''

# # for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g' ]:
# #     print (letter)

# # for y in ['p', 'y', 't', 'h', 'o', 'n']:
# #     print(f'Current value of y is: {y.upper ()}')

# # Every even number has a remainder of 0
# # Every odd number has a remainder of 1
# '''
# for x in range (1, 51) :
#     if x % 2 == 0:
#         print(x)

# #   =

# for y in range (2, 51, 2):
#     print(y)
# '''

############## While Loops ############################# While Loops ############################# While Loops ############################# While Loops ###############

# - CONDITION CONTROLLED repetition

# import time

# donuts = 10
# iz_hungeez = True


# while iz_hungeez:
#     donuts -= 1
#     if donuts > 0:
#         print(f'you ate a donut. There are {donuts} remaining.')
#         time.sleep(.7)
#     else: 
#         print(f'You\'ve Eaten all the Donuts! There are {donuts} remaining.')
#         iz_hungeez = False

############### Unicode ############################# Unicode ############################# Unicode ############################# Unicode ###############

# # Unicode (Icons and Emojis)
# print('\U0001F621')

############## Counters ############################# Counters ############################# Counters ############################# Counters ###############

# Count to 10

# import time

# # # Count up to 10
# # i = 1
# # while i < 11:
# #     print(i)
# #     i += 1
# #     time.sleep(.7)

# # # Count down from 10
# # j = 10
# # while j > 0:
# #     print(j)
# #     j -= 1
# #     time.sleep(.7)

# planets = [
#     'mercury',
#     'venus',
#     'earth',
#     'mars',
#     'jupiter',
#     'saturn',
#     'uranus',
#     'neptune',
#     'pluto',
# ]

# # This break causes the loop to terminate once Jupiter is printed
# # for planet in planets:
# #     time.sleep(.4)
# #     print(planet)
# #     if planet == 'neptune':
# #         break


# # Control mechnisms of our loops
# # - Break and continue
# # - The break statement acts as an emergency shutoff effectively killing the loop the instant the break is encountered
# # - The continue statement

# for planet in planets:
#     time.sleep(.4)
#     if planet == 'mars' and 'uranus':
#         continue
#     print(planet)