import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    '''Reads a csv file and returns a list of data rows'''
    fp = csv.reader(fp)
    data_rows = []
    next(fp, None)
    next(fp, None)
    next(fp, None)
    next(fp, None)
    for row in fp:
        if row[0] == '':
            continue
        else:
            data_rows.append(row)
    return data_rows


def get_totals(L):
    '''Returns the unauthorized immigrant population in the US and the sum of the other states'''
    us_pop = None
    total_pop = 0
    for row in L:
        if row[0] == 'U.S.':
            item = row[1].replace(',', '')
            us_pop = int(item)
        else:
            item = row[1].replace(',', '').replace('<', '')
            total_pop += int(item)
    return us_pop, total_pop


def get_largest_states(L):
    '''Returns a list of states whose value is greater than the summative value (the value in the row labeled “U.S.”)'''
    us_pop = L[0][2].replace('%', '')
    us_pop = float(us_pop)
    states = []
    for row in L:
        if row[0] != 'U.S.':
            item = row[2].replace('%', '')
            if float(item) > us_pop:
                states.append(row[0])
    states.sort()
    return states


def get_industry_counts(L):
    '''Returns a list of industries and occurrences in the column at index 9 (excluding the summative data from the row labeled “U.S.”)'''
    industry_counts = []
    for row in L:
        if row[0] != 'U.S.':
            if row[9] not in INDUSTRIES:
                continue
            else:
                industry = row[9]
            count = 1
            for i in range(len(industry_counts)):
                if industry_counts[i][0] == industry:
                    industry_counts[i][1] += 1
                    break
            else:
                industry_counts.append([industry, count])
    industry_counts.sort(key=itemgetter(1), reverse=True)
    return industry_counts


def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()