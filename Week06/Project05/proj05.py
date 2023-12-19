# Uncomment the following lines if you run the optional run_file tests locally
# so the input shows up in the output file. Do not copy these lines into Codio.
#
# import sys
# def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str


'''
CSE 231 Project 5

Algorithm:
    1. Ask the user for a filename
    2. Read the file and create a list of lists called network
    3. Calculate the similarity scores for each pair of users and create a similarity matrix
    4. Ask the user for a user_id
    5. Get friend recommendation by calling recommend()
    6. Display the suggested friend for the user that had max similarity score
    7. Prompt the user if they want to see the suggestion for another user or if they want to exit
'''

def open_file():
    '''
    Returns a file pointer to the file opened for reading
    File name is prompted from the user until a valid file name is entered
    Using a loop that continues to prompt the user until a valid file name is entered
    '''
    while True:
        file = input("\nEnter a filename: ")
        try:
            fp = open(file, "r")
            return fp
            break
        except FileNotFoundError:
            print("\nError in filename.")
            continue


def read_file(fp):
    '''
    Returns a list of lists that represents the network
    Finds it by reading the file line by line and creating a list of lists 
    where each element in the list is a list of friends for a user
    Args:
        fp: file pointer to the file opened for reading
    Returns:
        network: list of lists that represents the network
    '''
    # Read the file line by line
    Lines = fp.readlines()

    # Initialize count and network variables
    count = 0
    network = []

    # Create a list of lists where each element in the list is a list of friends for a user
    for line in Lines:
        count += 1
        if count == 1:
            # Get the number of users
            n = int(line.strip())

            # Create a list of size n
            network = [None] * n
        else:
            # Get the user and their friend
            user = line.split()
            u = int(user[0])
            v = int(user[1])

            # Add the friend to the user's list of friends
            if network[u] == None:
                network[u] = [v]
            else:
                network[u].append(v)

            if network[v] == None:
                network[v] = [u]
            else:
                network[v].append(u)
    return network


def num_in_common_between_lists(list1, list2):
    '''
    Returns the number of unique elements that are in both list1 and list2
    Args:
        list1: list of elements
        list2: list of elements
    Returns:
        count: number of unique elements that are in both list1 and list2
    '''
    # Get the length of the lists
    l1 = len(list1)
    l2 = len(list2)

    # Find the smaller and bigger lists
    if l1 < l2:
        length = l1
        smaller = list1
        bigger = list2
    else:
        length = l2
        smaller = list2
        bigger = list1

    # Count the number of unique elements that are in both list1 and list2
    count = 0
    for i in range(length):
        if smaller[i] in bigger:
            count += 1
    return count


def calc_similarity_scores(network):
    '''
    Returns a similarity matrix of size n x n
    Finds it by calculating the similarity score for each pair of users
    Args:
        network: list of lists that represents the network
    Returns:
        similarity_matrix: similarity matrix of size n x n
    '''
    # Get the number of users
    n = len(network)
    
    # Create a similarity matrix of size n x n
    similarity_matrix = [[0 for j in range(n)] for i in range(n)]

    # Calculate the similarity score for each pair of users
    for i in range(n):
        for j in range(n):
            # Call num_in_common_between_lists() to get the number of common friends
            num_in_common = num_in_common_between_lists(network[i], network[j])

            # Store the similarity score in the similarity matrix
            similarity_matrix[i][j] = num_in_common
            similarity_matrix[j][i] = num_in_common
    
    return similarity_matrix


def recommend(user_id, network, similarity_matrix):
    '''
    Returns the index of the user with the highest similarity score
    Finds it by finding the index of the largest similarity score
    Args:
        user_id: user id
        network: list of lists that represents the network
        similarity_matrix: similarity matrix of size n x n
    Returns:
        max_score_index: index of the user with the highest similarity score
    '''
    # Get the list of similarity scores for the given user_id
    similarity_scores = similarity_matrix[user_id]
    
    # Find the index of the largest similarity score
    max_score_index = similarity_scores.index(max(similarity_scores))
    
    # Check if the user with max_score_index is already a friend or is the same as user_id
    while max_score_index in network[user_id] or max_score_index == user_id:
        similarity_scores[max_score_index] = -1
        max_score_index = similarity_scores.index(max(similarity_scores))
    
    # Return the index of the user with the highest similarity score
    return max_score_index


def main():
    # Print welcome message
    print("Facebook friend recommendation.\n")
    
    # Call open_file() to get the file pointer
    fp = open_file()
    
    # Call read_file(fp) to get the list for the network
    network = read_file(fp)
    
    # Call calc_similarity_scores(network) to get the similarity matrix
    similarity_matrix = calc_similarity_scores(network)
    
    # Initialize user_input variable to 'yes'
    user_input = 'yes'

    # Repeat until user_input is 'no'
    while user_input.lower() != 'no':
        # Ask the user for a user_id
        user_id = input("\nEnter an integer in the range 0 to {}: ".format(len(network)-1))
        try:
            user_id = int(user_id)
        except ValueError:
            print("\nError: input must be an int between 0 and {}".format(len(network)-1))
            continue
        if user_id < 0 or user_id >= len(network):
            print("\nError: input must be an int between 0 and {}".format(len(network)-1))
            continue

        # Get friend recommendation
        friend_id = recommend(user_id, network, similarity_matrix)
        
        # Display the suggested friend for the user that had their id as user_id
        print("\nThe suggested friend for {} is {}".format(user_id, friend_id))
        
        # Prompt the user if they want to see the suggestion for another user input or if they want to exit
        user_input = input("\nDo you want to continue (yes/no)? ")


if __name__ == "__main__":
    main()