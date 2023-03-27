#MilesPerGallon calculation
from random import randint

#Function to get miles travelled per gallon
def mpg(miles, gallon):
    return miles//gallon

#get randum miles
miles_travelled=randint(200,400)
print("Miles travelled is: ",miles_travelled)
#get randum gallons
gallons_used=randint(10,25)
print("Gallons used is: ",gallons_used)

print("Car's MPG is: ",mpg(miles_travelled,gallons_used))



