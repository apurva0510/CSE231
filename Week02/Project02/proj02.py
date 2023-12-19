#CSE 231 PROJECT 2

#Algorithm
    #prompt the user for input on which function they want to run
    #use a while loop to check for input

    #Speed calculator
        #prompt the user for input on QPUs and angle of the slope
        #calculate and print speed

    #Parallel Universe Navigator
        #prompt the user for input on angle of the slope and mario speed
        #calculate DeFacto speed
        #use a for loop to check for valid quarter steps
        #if quarter step is valid, add to PU and find mario's position
            #else print quarter step is invalid
        #print PU and mario's position

    #Scuttlebug Transportation
        #prompt the user for input on mario's HP and coin distance
        #use a while loop to check for valid HP
        #use a while loop to whether or not Mario crosses the coin
        #use algebra to calculate distance travelled
        #print distance travelled

    #exit if user enters 'q'

import math

PU_SIZE = 65535
ISLAND = 1000
SCUTTLEBUG_RADIUS = 10
PROMPT = 0

while PROMPT != 'q':  
    PROMPT = input\
        ("\nSelect one of the following options:\n\
        1: Speed calculator\n\
        2: Parallel Universe navigator\n\
        3: Scuttlebug transportation\n\
        q: Exit the program\n\
        Option: ")

    if PROMPT == 'q':
        break

    if PROMPT == '1':
        QPU = int(input("\nHow many QPUs do you want to travel? "))
        ANGLE_str = input("\nWhat is the angle of the slope on which Mario is standing? ")
        ANGLE = float(ANGLE_str)
        speed = (QPU * PU_SIZE * 4) / math.cos(ANGLE)
        print("\nMario needs",round(speed),"speed") #print speed

    if PROMPT == '2':
        PU = 0
        Mario_pos = 0

        ANGLE_str = input("\nWhat is the angle of the slope on which Mario is standing? ")
        ANGLE = float(ANGLE_str)
        speed_new = int(input("\nWhat is Mario's speed? "))
        DeFacto = speed_new * math.cos(ANGLE) #DeFacto speed calculation
        
        for i in range (4):
            #ensure that the quarter step is valid
            if (0.25 * DeFacto) == PU_SIZE\
                 or abs(((0.25 * DeFacto) + Mario_pos) % PU_SIZE - PU_SIZE) < ISLAND:
                PU += (0.25 * DeFacto) / PU_SIZE

                #find mario's position in that PU
                if (0.25 * DeFacto) == PU_SIZE:
                    Mario_pos = 0
                else:
                    Mario_pos = (((0.25 * DeFacto) + Mario_pos) % PU_SIZE) - PU_SIZE

            else:
                print("\nQuarter step", i+1, "is invalid!")
                break

        if PU <= 1:
            print("\nMario has travelled", round(PU), "PU") #print PU
        else:
            print("\nMario has travelled", round(PU), "PUs") #print PUs

        print("Mario's position in this PU:", round(Mario_pos))
    
    if PROMPT == '3':
        distance = 0

        HP = int(input("\nWhat is Mario's current HP? "))
        #ensure that HP is valid
        while HP < 1 or HP > 8:
            print("\nInvalid amount of HP!")
            HP = int(input("\nWhat is Mario's current HP? "))
        
        COIN = int(input("\nAt what distance is the coin placed? Enter -1 if there is no coin. "))

        while HP != 0:
            if COIN == -1:
                distance += SCUTTLEBUG_RADIUS
                HP -= 1
            elif COIN < SCUTTLEBUG_RADIUS or COIN == distance:
                #only increase HP if it is less than 8
                if HP < 8:
                    HP += 1
                COIN = -1 #reset coin
                distance += SCUTTLEBUG_RADIUS
                HP -= 1
            else:
                distance += SCUTTLEBUG_RADIUS
                HP -= 1

        print("\nThe Scuttlebug can be transported", distance, "units of distance")