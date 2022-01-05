# Connect for time.date library 
from time import gmtime, strftime

print("Breakfast calories?")
Breakfast = int(input(int()))

print("Lunch calories?")
Lunch = int(input(int()))

print("Dinner calories?")
Dinner = int(input(int()))

print("Snack calories?")
Snack = int(input(int()))


print("Today date is " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))

sum = int(Breakfast + Lunch + Dinner + Snack)

print("Calorie content for " + strftime("%Y-%m-%d %H:%M    ") + str(sum))

# Done 5/5