# List
# my_list = ['red', 'blue', 'green']
# another_list = ['purple', 652, 'PIE'. False, 'g6df4g65df4g', 3, True]
# one_more_list = [1, 2, 3, 4, 5]

# Start                                                      # Flowcharts use symbols to represent steps in a program.
# Input hours worked                                         # Ovals are called terminal symbols, used to indicate the beginning and end of a program.
# Input hourly pay rate                                      # Parallelograms are called input symbols and output symbols. They represent steps in which the program reads input or displays output.
# Calculate gross pay as hours worked multiplied by pay rate # Rectangles are used as processing symbols. They represent steps in which the program performs some process on data, such as        mathematical calculation.
# Display gross pay                   # Rectangles are used as processing symbols. They represent steps in which the program performs some process on data, such as mathematical calculation.
# End

###### Employee Pay Calculator ######

# # Bonus Amount
# bonus = 500

# # Input the hours worked
# hours = float (input ('Please enter the hours worked by this employee: '))

# # Input the hourly rate
# pay = float (input ('Please enter the hourly pay rate for this employee: '))

# # Calculate gross pay
# gross = hours * pay

# # Bones Elegibility
# sales = float(input('Please enter Annual Sales Revenue: '))

# #Conditional objects 
# # if a condition does not create a false or true it will not print
# if sales > 70000:
#     bonus = 500
#     print('Nice job! You met the qouta!')
#     gross = gross + bonus
#     # OR gross += bonus

# # Display for gross pay
# print(f'${gross:2f} is the gross pay for the period.')

# Boolean Data Type
    # True or False values
    # (==) Equal check 
#        >         Greater Than
#        <         Less Than
#        >=        Greater Than or Equal To
#        ≤=        Less Than or Equal To
#        ==        Equals / Equality
#        !=        NOT Equals Than

# age = 9

# if age > 17:
# print ("You're an adult.")

# if 2 > 3:
# print("True")

# if 4 < 7:
# print("True")

# if 4 == 4:
# print("True")

# if 5 != 5:
# print("True")


# # Testing for multiple conditions #

# traffic_light = input('What color is the light? ')
# traffic_light = 'yellow'

# if traffic_light == 'red':
#     print("Stop.")

# elif traffic_light == 'Yellow':
#     print('Slow down.')

# else:
# print ("Step on it!")


# # # Tickets to the Circus
# # Children under the age of 4 get in for FREE!
# # Children 12 and under $12
# # Children Under 18 years old  $20
# # Adults $28
# # Seniors $15

# age = int(input( 'Please tell me your age: '))

# if age < 4:
#     print('your tickets is free!')
# if age < 13:
#     print('your tickets is $12!')
# if age < 18:
#     print('your tickets is $20!')
# if age < 65:
#     print('your tickets is $28!')
# else:
#     print('your ticket is $15')



#### WHEN YOU USE A SERIES OF IF STATEMENTS, YOU ARE TESTING FOR EVERY CONDITION 
#### TO TEST FOR ONE TRUE RESULT AND ONLY ONE, USE A SERIES OF ELIF STATEMENTS

# age = int(input( 'Please tell me your age: '))

# if age < 4:
#     print("Your ticket is FREE!")

# elif age < 13:
#     print("Your ticket is $12!")

# elif age < 18:
#     print("Your ticket is $20!")

# elif age < 65:
#     print("Your ticket is $28!")

# else:
#     print("Your ticket is $15")

# CLEANER VERSION #

# age = int(input( 'Please tell me your age: '))

# if age < 4:
#     price = 'Free'

# elif age < 13:
#     price = 12

# elif age < 18:
#     price = 20

# elif age < 65:
#     price = 28

# # Else will catch anything that isnt caught in the if or elif
# else:
#     price = 15


# print(f'Your ticket will cost ${price}')

# String comparison
fav_day = 'Tuesday'
if fav_day == 'tuesday':
    print('Taco Tuesday!!!')

if 'Tuesday' == 'tuesday':
    print('Same')

else:
    print('diffrent')