# QUIZ 1
# Use variables to print sentances below

# 1. name of variable : station
# 2. value of variable : "Queens Bound", "Manhattan Bound", "Bronx Bound"
# : The train for XX Bound is now approaching
station = "Queens Bound"
print("The train for",station,"is now approaching")

# QUIZ 2 

'''You made a new coding community recently. 
You make a meetings four times in a month, three time is on online and rest is offline. 
Make a program that select offline meeting date fit into evidence below.'''

# 1. have to select date randomly
# 2. consider number of day is different from month to month, maximun is 28
# 3. exclude 1st ~ 3rd of each month during the ready for study

# (printout example)
# offline study date is selected to Xth each month.

from random import *
date = randint(4,28)
print("offline study date is selected to" +str(date))
