
# An index error means Python can’t find an item at the index you requested. 
# If an index error occurs in your program, try adjusting the index you’re asking for by one. 
# Then run the program again to see if the results are correct.

#Keep in mind that whenever you want to access the last item in a list, you should use the index -1. 
# This will always work, even if your list has changed size since the last time you accessed it:

Names = ['Beth', 'Malorie', 'Madison', 'Alex']

print(Names[4]) # "4" is not in the range of the list 