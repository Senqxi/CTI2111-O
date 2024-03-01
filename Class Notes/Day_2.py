# # Week 1 Day 2

# # Topics
# # -Concatenation
# # -f-strings
# # -String Method
# # -Input Function
# # -Variable Casting


# # -- String Concatenation --
# first_name = "thomas"
# last_name = "anderson"
# # the " = " symbol is used to assign operations
# # concatenation connects one or more strings to each other
# print(first_name + " " + last_name)

# # Variable Casting

# ''' 
# str()     <------Converts variable to String
# int()     <------Converts variable to Interger
# float()   <------Converts variable to Floats
# list()    <------Converts variable to List
# bool()    <------Converts variable to Boolean
# '''

# # Addition (+) Operator has two jobs
# #  - connect two or more strings together -REQUIRES STRING-
# #  - performs additions -REQUIRES NUMBERS-
# #  - CANNOT USE THIS BETWEEN A STRING AND A NUMBER 

# # String Method
# # All string methods return new values. They DO NOT CHANGE the original string 
# # String methods are used just for that instance not the whole code 
# '''
# capitalize()	Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	    Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()     	Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isascii()	    Returns True if all characters in the string are ascii characters
# isdecimal()  	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()  	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()   	Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()	        Converts the elements of an iterable into a string
# ljust()       	Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()     	Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	        Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()     	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()   	Swaps cases, lower case becomes upper case and vice versa
# title()	        Converts the first character of each word to upper case
# translate()	    Returns a translated string
# upper()     	Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning
# '''
# # - A method is a function that "belongs" to an object
# # Objects Python Reference
# '''
# Python String Methods
# Python List Methods
# Python Dictionary Methods
# Python Tuple Methods
# Python Set Methods
# Python File Methods
# '''
# # Collecting information from users
# # We use the input() Function to prompt users to supply the information that we need

# # Capture user name
# name = input("Hello, What is your name?" + " ")
# print("Nice to meet you" + " " + name + ".")

# # Capture user age
# age = input("please tell me your age." + " ")
# print("Wow. You are" + " " + age + " " + "years old!")

# # F-String
# # - format strings
# # - more readable
# # - faster
# # - less prone to mistakes
# # - more concise
# print(f"My first name is {first_name} and my last name is {last_name}")
# print("My first name is " + first_name + " and my last name is " + last_name)


########################################################################################### DEMO ############################################################################################


# Create Shopping List Variables
shoes_price = 199.99
chicken_thighs_price = 4.59
chicken_breasts_price = 9.99
milk_price = 4.99
eggs_price = 3.49

# Prompt the userfor quantities
shoes = int( input("How many pairs of shoes would you like?\n"))
chicken_thighs = int( input("How many pairs of chicken thighs would you like?\n"))
chicken_breasts = int( input("How many pairs of chicken breast would you like?\n"))
milk = int( input("How many pairs of milk would you like?\n"))
eggs = int( input("How many pairs of eggs would you like?\n"))

# # (') can replace (") so that we can use quotations
# print('In the movie, Arnold said, "I\'ll be back!"')

# Cost of Items
cost_of_items = (shoes * shoes_price) + (chicken_breasts * chicken_breasts) + (chicken_thighs * chicken_thighs_price) + (milk * milk_price) + (eggs * eggs_price)
print (cost_of_items)

# Tax Rate
tax_rate = 0.065

# Calculate Sub-Total
tax = cost_of_items * tax_rate
print (tax)

# Out the Door
total = tax + cost_of_items
print (total)

# Thank Customer
print(f"Thanks for shopping with us today. Your total amount is ${total:.2f} and we appreciate your business! Have a nice day.")

########################################################################################### DEMO ############################################################################################
