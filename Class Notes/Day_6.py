
# # Functions Review
# # def c_k(c):
# #     k = c + 273.15 
# #     return k

# # print(c_k(2))


# ############## Error Handling ############################# Error Handling ############################# Error Handling ############################# Error Handling ############################# Error Handling ###############

# # Request a user provides 2 numbers
# num1 = int(input('Please provide a number in numeric format: '))
# num2 = int(input('Please provide another number in numeric format: '))

# # The variable rebresents the quotient of the 2 inputed numbers
# result = num1 /num2
# print(f'{num1} divided by {num2} is {result}')

# # An error could be produced if num (divisor) == 0
# # To prevent this or other errors we can craft our program in a way to avoid these errors/exceptions

# # The if statement will test the value of num2 and display an error if the number is zero
# if num2 != 0:
#     result = num1 / num2
#     print(f'{num1} divided by {num2} is {result}')
# else:
#     print("Cannot divide by zero!")

# # Sometimes no matter how careful we are, some exceptions just can't be avoided
# # This is where exception handling comes in
# # An exception is an error that occurs while a program is running, causing it to crash
# # Python uses try and except statement to handle these exceptions

# ##############   #############################   #############################   #############################

# try:
# # Request a user provides 2 numbers
#     num1 = int(input( 'Please provide a number in numeric format: ' ))
#     num2 = int(input( 'Please provide another number in numeric format: '))
#     # Return the quotient of the 2 user-provided numbers
#     result = num1 / num2
#     print(f'{num1} divided by {num2} is {result}')
    
# except ZeroDivisionError:
#     print ("Cannot divide by zero!")

# except ValueError:
#     print( 'Numbers must be in numeric format. Please read the directions!')



# try:
#     age = int(input('Please enter your age: '))
#     income = 80000
#     risk = income / age

# except ValueError:
# except ZeroDivisionError:

################# Advanced Example ################################# Advanced Example ################################# Advanced Example ################################# Advanced Example ################

# guitars = ['stratocaster' ,'telecaster' ,'les paul' ,'sg' ,'rg' ,'schecter', 'epiphone', 'prs']
# print(guitars)

# try:
#     selection = input( 'What\'s your favorite guitar in this list? \n')
#     if selection not in guitars:
#         raise ValueError
#     else:
#         print(f'The {selection.title()} is a great choice!!')

# except:
#     print('choose onl;y the available options')


################# Advanced Example ################################# Advanced Example ################################# Advanced Example ################################# Advanced Example ################


attempts = 5

while True:
    guitars = ['stratocaster', 'telecaster', 'les paul', 'sg', 'rg', 'schecter', 'epiphone', 'prs']
    print (guitars)

    if attempts > 0:
        try:
            selection = input ( 'What\'s your favorite guitar in this list? \n' )
            selection = selection. lower ()
            if selection not in guitars:
                raise ValueError 

            else:
                print(f'The {selection.title()} is a great choice!')
                break
        except ValueError:
            print('You chose poorly. Please select from the list of available options.')

        attempts -= 1

    else:
        print ('Out of attempts.')
        break