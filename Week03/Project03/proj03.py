#CSE 231 PROJECT 3

#Algorithm
    #define constants values
    #define constant strings

    #while loop to keep the program running until user enters 'N'
        #print welcome text and main prompt
        #input location and convert to uppercase
                #initialize price per square foot and property tax rate based on location
                #if location is not known, use national averages

        #input square footage
        #input max monthly payment
            #if max monthly payment is not known, set case to 1
        #input down payment
        #input APR
            #if APR is not known, set case to 2
        #if square footage and max monthly payment are not known, set case to 4
        #if square footage is not known, set case to 3
            #find square footage
                #initialize max square footage to 100
                #if mortgage is less than or equal to max monthly payment, increase square footage by 1
                #else, decrease square footage by 1 and break
        
        #calculate monthly payment and monthly property tax
        #format values (capitalize, add commas, etc.)

        #if case is 1 or 2
            #for unkown location, print location not known text and set location to 'the average U.S. housing market'
            #print house cost, mortgage, and 
            #if case is 2
                #whether or not the user can afford the house
            #input whether or not the user wants to print the amortization table
                #if yes, print table
                    #print table header
                    #print table divider
                    #for loop to print table values
                        #calculate interest and payment
                        #print values
                        #calculate new balance
        #if case is 3
            #print house cost, square footage, and max monthly payment
        #if case is 4
            #print not enough information text
        
        #input whether or not the user wants to continue the program
            #if 'N', break

NUMBER_OF_PAYMENTS = 360    # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

KEEP_GOING = 'Y'

WELCOME_TEXT = '''\nMORTGAGE PLANNING CALCULATOR\n============================ '''
MAIN_PROMPT = '''\nEnter a value for each of the following items or type 'NA' if unknown '''
LOCATIONS_TEXT = '''\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? '''
SQUARE_FOOTAGE_TEXT = '''\nWhat is the maximum square footage you are considering? '''
MAX_MONTHLY_PAYMENT_TEXT = '''\nWhat is the maximum monthly payment you can afford? '''
DOWN_PAYMENT_TEXT = '''\nHow much money can you put down as a down payment? '''
APR_TEXT = '''\nWhat is the current annual percentage rate? '''
AMORTIZATION_TEXT = '''\nWould you like to print the monthly payment schedule (Y or N)? '''
LOCATION_NOT_KNOWN_TEXT = '''\nUnknown location. Using national averages for price per square foot and tax rate.'''
NOT_ENOUGH_INFORMATION_TEXT = '''\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.'''
KEEP_GOING_TEXT = '''\nWould you like to make another attempt (Y or N)? '''

while KEEP_GOING != 'N':
    #initializing variables
    CASE = 2
    home_cost = 0
    P = 0

    print(WELCOME_TEXT)
    print(MAIN_PROMPT)

    #Location input
    location = input(LOCATIONS_TEXT)
    location = location.upper()

    if location == 'SEATTLE':
        PRICE_PER_SQ_FOOT = SEATTLE_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = SEATTLE_PROPERTY_TAX_RATE

    elif location == 'SAN FRANCISCO':
        PRICE_PER_SQ_FOOT = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = SAN_FRANCISCO_PROPERTY_TAX_RATE

    elif location == 'AUSTIN':
        PRICE_PER_SQ_FOOT = AUSTIN_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = AUSTIN_PROPERTY_TAX_RATE

    elif location == 'EAST LANSING':
        PRICE_PER_SQ_FOOT = EAST_LANSING_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = EAST_LANSING_PROPERTY_TAX_RATE
        
    else:
        PRICE_PER_SQ_FOOT = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT
        PROPERTY_TAX_RATE = AVERAGE_NATIONAL_PROPERTY_TAX_RATE

    #Square footage input
    square_footage = input(SQUARE_FOOTAGE_TEXT)

    #Max monthly payment input
    max_monthly_payment = input(MAX_MONTHLY_PAYMENT_TEXT)
    if max_monthly_payment == 'NA':
        CASE = 1
        max_monthly_payment = 0
    max_monthly_payment = float(max_monthly_payment)

    #Down payment input
    down_payment = int(input(DOWN_PAYMENT_TEXT))

    #APR input
    apr = input(APR_TEXT)
    if apr == 'NA':
        apr = APR_2023
        apr = float(apr)
    else:
        apr = float(apr)
        apr = apr / 100

    if square_footage == 'NA' and max_monthly_payment == 0:
        CASE = 4

    #finding square footage (case 3)
    if square_footage == 'NA':
        CASE = 3
        max_footage = 100

        home_cost = max_footage * PRICE_PER_SQ_FOOT
        P = home_cost - down_payment
        MONTHLY_APR = apr / 12
        MONTHLY_PAYMENT = (P * (MONTHLY_APR * ((1 + MONTHLY_APR) ** NUMBER_OF_PAYMENTS))) / \
            (((1 + MONTHLY_APR) ** NUMBER_OF_PAYMENTS) - 1)
        MONTHLY_PROPERTY_TAX = (home_cost * PROPERTY_TAX_RATE) / 12
        mortgage = MONTHLY_PAYMENT + MONTHLY_PROPERTY_TAX

        while mortgage < max_monthly_payment:

            home_cost = max_footage * PRICE_PER_SQ_FOOT
            P = home_cost - down_payment
            MONTHLY_APR = apr / 12
            MONTHLY_PAYMENT = (P * (MONTHLY_APR * ((1 + MONTHLY_APR) ** NUMBER_OF_PAYMENTS))) / \
                (((1 + MONTHLY_APR) ** NUMBER_OF_PAYMENTS) - 1)
            MONTHLY_PROPERTY_TAX = (home_cost * PROPERTY_TAX_RATE) / 12
            mortgage = MONTHLY_PAYMENT + MONTHLY_PROPERTY_TAX

            if mortgage > max_monthly_payment:
                max_footage = max_footage - 1
                break
            else:
                max_footage = max_footage + 1

        square_footage = max_footage
    square_footage = int(square_footage)

    #calculations
    home_cost = square_footage * PRICE_PER_SQ_FOOT
    P = home_cost - down_payment
    MONTHLY_APR = apr / 12
    MONTHLY_PAYMENT = (P * (MONTHLY_APR * ((1 + MONTHLY_APR) ** NUMBER_OF_PAYMENTS))) / \
        (((1 + MONTHLY_APR) ** NUMBER_OF_PAYMENTS) - 1)
    MONTHLY_PROPERTY_TAX = (home_cost * PROPERTY_TAX_RATE) / 12
    mortgage = MONTHLY_PAYMENT + MONTHLY_PROPERTY_TAX
    B = mortgage

    #formatting
    location = location.capitalize()

    square_footage = '{:,}'.format(int(square_footage))
    home_cost = '{:,}'.format(int(home_cost))
    down_payment = '{:,}'.format(int(down_payment))

    apr = apr * 100
    apr = '{:.1f}'.format(apr)

    PAYMENT = MONTHLY_PAYMENT
    MONTHLY_PAYMENT = '{:,.2f}'.format(MONTHLY_PAYMENT)
    MONTHLY_PROPERTY_TAX = '{:,.2f}'.format(MONTHLY_PROPERTY_TAX)
    mortgage = '{:,.2f}'.format(mortgage)

    #case 1 and 2
    if CASE == 1 or CASE == 2:
        if location not in ['Seattle', 'San francisco', 'Austin', 'East lansing']:
            print(LOCATION_NOT_KNOWN_TEXT)
            location = 'the average U.S. housing market'
            
        print('\n\nIn {}, an average {} sq. foot house would cost ${}.'\
            .format(location, square_footage, home_cost))
        print('A 30-year fixed rate mortgage with a down payment of ${} at {}% APR results'\
            .format(down_payment, apr))
        print('\tin an expected monthly payment of ${} (taxes) + ${} (mortgage payment) = ${}'\
            .format(MONTHLY_PROPERTY_TAX, MONTHLY_PAYMENT, mortgage))

        if CASE == 2:
            if float(max_monthly_payment) >= float(B):
                print('Based on your maximum monthly payment of ${:,.2f} you can afford this house.'\
                    .format(max_monthly_payment))
            else:
                print('Based on your maximum monthly payment of ${:,.2f} you cannot afford this house.'\
                    .format(max_monthly_payment))
        
        #table
        amortization = input(AMORTIZATION_TEXT)
        amortization = amortization.upper()

        if amortization == 'Y':
            print('\n{:^7s}|{:^12s}|{:^13s}|{:^14s}'.format('Month', 'Interest', 'Payment', 'Balance'))
            print('=' * 48)
            for i in range(1, 361):
                interest = P * MONTHLY_APR
                payment = PAYMENT - interest
                print('{:^7d}| ${:>9,.2f} | ${:>10,.2f} | ${:>11,.2f}'.format(i, interest, payment, P))
                P = P - payment
    
    elif CASE == 3:
        print('\nIn {}, a maximum monthly payment of ${:,.2f} allows the purchase of a house of {} sq. feet for ${}'\
            .format(location, max_monthly_payment, square_footage, home_cost))
        print('\tassuming a 30-year fixed rate mortgage with a ${} down payment at {}% APR.'\
            .format(down_payment, apr))

    elif CASE == 4:
        print(NOT_ENOUGH_INFORMATION_TEXT)

    #determine if user wants to continue the program
    KEEP_GOING = input(KEEP_GOING_TEXT)
    KEEP_GOING = KEEP_GOING.upper()
    if KEEP_GOING == 'N':
        break
    elif KEEP_GOING == 'Y':
        continue