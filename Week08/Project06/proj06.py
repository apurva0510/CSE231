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

# CSE 231 Project 6

# Algorithm:
#     1. Prompt the user for a filename for the stop words
#     2. Read the stop words from the file
#     3. Prompt the user for a filename for the song data
#     4. Read the song data from the file
#     5. Calculate the average word count for every singer
#     6. Calculate the vocabulary size for every singer
#     7. Combine the dictionaries into a list of tuples in the format (singer name, number of songs, average word count, vocabulary size)
#     8. Display the top 10 singers by average word count
#     9. Prompt the user for a set of words to search through lyrics until the user presses enter
#     10. Convert the input to a set of words
#     11. Convert the words to lowercase
#     12. Search for songs containing the given words
#     13. Validate the words for digits, punctuation and stop words
#     14. Print the number of songs containing the given words only if there are any

import csv
import string
from operator import itemgetter

def open_file(message):
    '''
    Returns a file pointer to the file opened for reading
    File name is prompted from the user until a valid file name is entered
    Using a loop that continues to prompt the user until a valid file name is entered
    '''
    while True:
        # Prompt the user for a filename
        filename = input(message)
        # Try to open the file
        try:
            fp = open(filename)
            return fp
        # If the file cannot be opened, print an error message and prompt the user for another filename
        except FileNotFoundError:
            print("Error: File not found. Please try again.")


def read_stopwords(fp):
    '''
    Returns a set of words from the given file pointer.
    Stopwords are read from the file line by line and added to a set.
    Args: 
        fp: file pointer to the file opened for reading
    Returns:
        stopwords: set of words from the given file pointer
    '''
    # Initialize stopwords set
    stopwords = set()

    # Read the file line by line and add the words to the stopwords set
    for line in fp:
        line = line.strip().lower()
        stopwords.add(line)

    fp.close()

    return stopwords
        

def validate_word(word, stopwords):
    '''Returns True if the given word is not in the stop word set and has no digits or punctuation.'''
    return word.isalpha() and word not in stopwords


def process_lyrics(lyrics, stopwords):
    ''' 
    Returns a set of words by processing song lyrics and removing stopwords from it.
    Args:
        lyrics: a string of lyrics
        stopwords: a set of stopwords
    Returns:
        words_set: a set of words from the given lyrics string
    '''
    # Initialize words_set
    words_set = set()
    # Split the lyrics string into words
    words = lyrics.split()

    # Add the words to the words_set if they are valid
    for word in words:
        word = word.lower().strip(string.whitespace + string.punctuation)
        if validate_word(word, stopwords):
            words_set.add(word)

    return words_set


def update_dictionary(data_dict, singer, song_name, song_words_set):
    ''' 
    Inserts a song_name: song_words_set key-value pair to the song_dict dictionary of the singer.
    Args:
        data_dict: a dictionary of singers (the key), and each value is a dictionary of all the signer's songs (song_dict)
        singer: singer's name
        song_name: song's name
        song_words_set: a set of words
    Returns:
        None
    '''
    # If the singer is not in the data_dict, add the singer to the data_dict
    if singer not in data_dict:
        data_dict[singer] = {}
    # If the song_name is not in the singer's song_dict, add the song_name and song_words_set to the song_dict
    data_dict[singer][song_name] = song_words_set


def read_data(fp, stopwords):
    '''
    Reads in the data from the csv file and returns a dictionary of singers, songs and their words.
    Args:
        fp: file pointer for a csv file
        stopwords: a set of stop words
    Returns:
        data_dict: a dictionary of singers, songs and their words
    '''
    # Initialize data_dict
    data_dict = {}
    # Read the csv file
    reader = csv.reader(fp)
    next(reader) # skip headers

    # Process the lyrics for every song and add them to the data_dict
    for row in reader:
        # Get the singer, song_name and lyrics
        singer = row[0]
        song_name = row[1]
        lyrics = row[2].lower()
        # Process the lyrics and get the words_set
        song_words_set = process_lyrics(lyrics, stopwords)
        # Update the data_dict
        update_dictionary(data_dict, singer, song_name, song_words_set)
        
    fp.close()
    return data_dict


def calculate_average_word_count(data_dict):
    ''' 
    Calculates the average word count for each singer in the data_dict.
    Args:
        data_dict: a dictionary of singers, songs and their words
    Returns:
        singer_word_count: a dictionary of singers and their average word count
    '''
    # Initialize singer_word_count
    singer_word_count = {}

    for singer, songs in data_dict.items():
        # Initialize total_word_count and song_count
        total_word_count = 0
        song_count = 0

        # Calculate the total word count and song count for the singer
        for song_name, song_words_set in songs.items():
            total_word_count += len(song_words_set)
            song_count += 1

        # Calculate the average word count for the singer
        average_word_count = total_word_count / song_count
        singer_word_count[singer] = average_word_count

    return singer_word_count


def find_singers_vocab(data_dict):
    ''' 
    Returns a dictionary containing the set of distinct words used by every singer.
    Args:
        data_dict: a dictionary of singers, songs and their words
    Returns:
        singers_vocab: a dictionary containing the set of distinct words used by every singer
    '''
    # Initialize singers_vocab
    singers_vocab = {}

    # Find the set of distinct words used by every singer
    for singer, songs in data_dict.items():
        vocab_set = set()

        # Add the unique words to the vocab_set
        for song_name, song_words_set in songs.items():
            vocab_set = vocab_set.union(song_words_set)

        # Add the singer and their vocab_set to the singers_vocab dictionary
        singers_vocab[singer] = vocab_set

    return singers_vocab


def display_singers(combined_list):
    ''' 
    Sorts the list by average word count in descending order. 
    If two tuples have the same average, it sorts them by the vocabulary size, again in descending order. 
    If two tuples have the same average and same vocabulary size, it keeps the same order as it appears in the combined_list list. 
    Finally, it prints the top ten tuples after sorting the list in the given format.
    Args:
        combined_list: a list of tuples for every singer containing (singer name, average word count, number of songs, vocabulary size)
    Returns:
        None
    '''
    # Sort the list by average word count in descending order
    # If two tuples have the same average, sort them by vocabulary size in descending order
    # If two tuples have the same average and same vocabulary size, keep the same order as it appears in the combined_list list
    sorted_list = sorted(combined_list, key=itemgetter(1, 3), reverse=True)

    # Print the header
    print("\n{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs"))
    print('-' * 80)

    # Print the top ten tuples
    for i in range(min(10, len(sorted_list))):
        singer, avg_word_count, num_songs, vocab_size = sorted_list[i]
        avg_word_count = round(avg_word_count, 2)
        vocab_size = len(vocab_size)
        print("{:<20s}{:>20.2f}{:>20d}{:>20d}".format(singer, avg_word_count, vocab_size, num_songs))


def search_songs(data_dict, words):
    '''
    Returns a list of tuples (singer name, song name) for every song that includes every word in the given word set.
    Args:
        data_dict: a dictionary of singers, songs and their words
        words: a set of words to search for in the songs
    Returns:
        matched_songs: a list of tuples (singer name, song name) for every song that includes every word in the given word set
    '''
    # Initialize matched_songs
    matched_songs = []

    # If the words are in the song_words_set, add the song to the matched_songs list
    for singer, songs in data_dict.items():
        for song_name, song_words_set in songs.items():
            if words.issubset(song_words_set):
                matched_songs.append((singer, song_name))
    
    # Sort the matched_songs list by singer name and then by song name
    sorted_matched_songs = sorted(matched_songs, key=lambda x: (x[0], x[1]))

    return sorted_matched_songs


def main():
    # Prompt the user for a filename for the stop words
    stop_words_file = open_file('\nEnter a filename for the stopwords: ')

    # Read the stop words from the file
    stop_words = read_stopwords(stop_words_file)

    # Prompt the user for a filename for the song data
    song_data_file = open_file('\nEnter a filename for the song data: ')

    # Read the song data from the file
    song_data = read_data(song_data_file, stop_words)

    # Calculate the average word count for every singer
    avg_word_count_dict = calculate_average_word_count(song_data)

    # Calculate the vocabulary size for every singer
    vocab_dict = find_singers_vocab(song_data)

    # Combine the dictionaries into a list of tuples in the format (singer name, number of songs, average word count, vocabulary size)
    combined_list = []
    for singer in song_data.keys():
        num_songs = len(song_data[singer])
        avg_word_count = avg_word_count_dict[singer]
        vocab_size = vocab_dict[singer]
        combined_list.append((singer, avg_word_count, num_songs, vocab_size))

    # Display the top 10 singers by average word count
    display_singers(combined_list)

    # Prompt the user for a set of words to search through lyrics
    words_input = input("\nSearch Lyrics by Words\n\nInput a set of words (space separated), press enter to exit: ")
    while words_input:
        # Convert the input to a set of words
        words = set(words_input.split())

        # Convert the words to lowercase
        words = set(word.lower() for word in words)

        # Search for songs containing the given words
        matched_songs = search_songs(song_data, words)

        # Validate the words for digits, punctuation and stop words
        if stop_words.intersection(words) or not all(validate_word(word, stop_words) for word in words):
            print("\nError in Words!")
            print("1-) Words should not have any digit or punctuation")
            print("2-) Word list should not include any stop-word")
        else:
            # Print the number of songs containing the given words
            print("\nThere are {} songs containing the given words!".format(len(matched_songs)))

        # Print the matched songs only if there are any
        if len(matched_songs) > 0:
            print("{:<20s} {:<s}".format("Singer", "Song"))
            for singer, song_name in matched_songs[:5]:
                print("{:<20s} {:<s}".format(singer, song_name))

        # Prompt the user for another set of words to search through lyrics
        words_input = input("\nInput a set of words (space separated), press enter to exit: ")




if __name__ == '__main__':
    main()       