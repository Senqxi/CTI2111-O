
################ 3-10. Every Function ####################

# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

import os 

os.system('Clear')
print("-"*37)

# Create a list of countries
countries = ["USA", "Canada", "Australia", "Japan", "Brazil"]

# Print the original list
print("Original list of countries:", countries)
print("-"*37)

# Append a new country to the list
countries.append("Germany")
print("List after appending a new country:", countries)
print("-"*37)

# Insert a country at a specific position
countries.insert(2, "China")
print("List after inserting a country:", countries)
print("-"*37)

# Remove a country from the list
removed_country = countries.pop(3)
print("List after removing a country:", countries)
print("-"*37)

# Remove a specific country from the list
countries.remove("Brazil")
print("Let us remove Brazil")
print("List after removing a specific country:", countries)
print("-"*37)

# Sort the list in alphabetical order
countries.sort()
print("List after sorting in alphabetical order:", countries)
print("-"*37)

# Reverse the order of the list
countries.reverse()
print("List after reversing the order:", countries)
print("-"*37)

# Get the length of the list
num_countries = len(countries)
print("Number of countries in the list:", num_countries)
print("-"*37)

# Access elements of the list using index
print("First country in the list:", countries[0])
print("-"*37)
print("Last country in the list:", countries[-1])
print("-"*37)

# Clear the list
countries.clear()
print("List after clearing:", countries)
print("-"*37)
