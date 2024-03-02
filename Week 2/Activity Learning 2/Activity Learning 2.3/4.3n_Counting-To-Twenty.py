
################### Making Numerical Lists ####################

# Many reasons exist to store a set of numbers. 
# For example, you’ll need to keep track of the positions of each character in a game, and you might want to keep track of a player’s high scores as well. 

# In data visualizations, you’ll almost always work with sets of numbers, such as temperatures, distances, population sizes, 
# or latitude and longitude values, among other types of numerical sets.

# Lists are ideal for storing sets of numbers, and Python provides a variety of tools to help you work efficiently with lists of numbers. 
# Once you understand how to use these tools effectively, your code will work well even when your lists contain millions of items.

################### Using the range() Function ###################

# Python’s range() function makes it easy to generate a series of numbers. 
# For example, you can use the range() function to print a series of numbers like this:

'''
first_numbers.py

for value in range(1, 5):
    print(value)
'''

# Although this code looks like it should print the numbers from 1 to 5, it doesn’t print the number 5:

'''
1
2
3
4
'''

# In this example, range() prints only the numbers 1 through 4. 
# This is another result of the off-by-one behavior you’ll see often in programming languages. 
# The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. 
# Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.

'''
first_numbers.py

for value in range(1, 6):
    print(value)
'''

# This time the output starts at 1 and ends at 5:

'''
1
2
3
4
5 <----- # This was added
'''

# You can also pass range() only one argument, and it will start the sequence of numbers at 0. 
# For example, range(6) would return the numbers from 0 through 5.

####################### Using range() to Make a List of Numbers #########################

# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. 
# When you wrap list() around a call to the range() function, the output will be a list of numbers.

# In the example in the previous section, we simply printed out a series of numbers. We can use list() to convert that same set of numbers into a list:

'''
numbers = list(range(1, 6))
print(numbers)
'''

#This is the result:
'''
[1, 2, 3, 4, 5]
'''
# We can also use the range() function to tell Python to skip numbers in a given range. 
# If you pass a third argument to range(), Python uses that value as a step size when generating numbers.

# For example, here’s how to list the even numbers between 1 and 10:

'''
even_numbers.py

even_numbers = list(range(2, 11, 2))
print(even_numbers)
'''

# In this example, the range() function starts with the value 2 and then adds 2 to that value. 
# It adds 2 repeatedly until it reaches or passes the end value, 11, and produces this result:

'''
[2, 4, 6, 8, 10]
'''

# You can create almost any set of numbers you want to using the range() function. 
# For example, consider how you might make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). 
# In Python, two asterisks (**) represent exponents. Here’s how you might put the first 10 square numbers into a list:

'''
square_numbers.py

squares = []
for value in range(1, 11):
❶     square = value ** 2
❷     squares.append(square)

print(squares)
'''

# We start with an empty list called squares. 
# Then, we tell Python to loop through each value from 1 to 10 using the range() function. 
# Inside the loop, the current value is raised to the second power and assigned to the variable square ❶. 
# Each new value of square is then appended to the list squares ❷. 
# Finally, when the loop has finished running, the list of squares is printed:

'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

# To write this code more concisely, omit the temporary variable square and append each new value directly to the list:

'''
squares = []
for value in range(1,11):
    squares.append(value**2) <-- Added the Variable into the function

print(squares)
'''

# This line does the same work as the lines inside the for loop in the previous listing. 
# Each value in the loop is raised to the second power and then immediately appended to the list of squares.

# You can use either of these approaches when you’re making more complex lists. 
# Sometimes using a temporary variable makes your code easier to read; 
# other times it makes the code unnecessarily long. 
# Focus first on writing code that you understand clearly, and does what you want it to do. 
# Then look for more efficient approaches as you review your code.

################ Simple Statistics with a List of Numbers ###################

# A few Python functions are helpful when working with lists of numbers. 
# For example, you can easily find the minimum, maximum, and sum of a list of numbers:

'''
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

>>> min(digits)
0

>>> max(digits)
9

>>> sum(digits)
45

'''

#################### List Comprehensions ####################

# The approach described earlier for generating the list squares consisted of using three or four lines of code. 
# A list comprehension allows you to generate this same list in just one line of code. 
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.

'''
squares.py

squares = [value**2 for value in range(1, 11)]
print(squares)
'''

# To use this syntax, begin with a descriptive name for the list, such as squares. 

# Next, open a set of square brackets and define the expression for the values you want to store in the new list. 
# In this example the expression is value**2, which raises the value to the second power. 

# Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. 
# The for loop in this example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2. 

# Note that no colon is used at the end of the for statement.

'''
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

##############  #############################  #############################  #############################  #############################  #############################  ###############

# 4-3. Counting to Twenty: 

# Use a for loop to print the numbers from 1 to 20, inclusive.

import os 

os.system('Clear')
print("-"*37)

for value in range(1, 21):
    print(value)
