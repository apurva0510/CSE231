#CSE 231 PROJECT 1

#Algorithm
    #prompt for a float input in rods
    #use arithmetic functions to convert rods to other units
    #s=(d/t)*60 to calculate time in minutes
    #confirm input rods
    #print conversions and time

import math

#use the following strings in your input and print statements
rods = float(input("Input rods: "))

RODS_TO_METERS = 5.0292     #1 rod  = 5.0292 meters
meters = rods * RODS_TO_METERS

METERS_TO_FEET = 0.3048     #1 foot = 0.3048 meters
foot = meters / METERS_TO_FEET

METERS_TO_MILES = 1609.34   #1 mile = 1609.34 meters
mile = meters / METERS_TO_MILES

RODS_TO_FURLONG = 40        #1 furlong  = 40 rods
furlong = rods / RODS_TO_FURLONG

AVG_SPEED = 3.1             #average walking speed is 3.1 miles per hour 
time = (mile / AVG_SPEED) * 60  

#the following 2 strings should be in the same print statement
#seperated by the input rods
print("\nYour value is", rods,\
    "rods.\n")

print("Conversions"\
    "\nMeters:", round(meters, 3),\
    "\nFeet:", round(foot, 3),\
    "\nMiles:", round(mile, 3),\
    "\nFurlongs:", round(furlong, 3),\
    "\nMinutes to walk", rods,\
    "rods:", round(time, 3))