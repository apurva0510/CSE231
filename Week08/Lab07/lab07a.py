import string
from operator import itemgetter


def add_word(word_map, word):
    #add word to the map if it is not there
    if word not in word_map:
        word_map[word] = 1
    else:
        #increment the word count
        word_map[word] += 1


def build_map(in_file, word_map):
    for line in in_file:

        #initialize a list of words
        word_list = line.split()

        for word in word_list:
            #strip off whitespace and punctuation
            word = word.strip().strip(string.punctuation)
            word = word.lower()
            if word == " " or word == "":
                continue
            else:
                add_word(word_map, word)


def display_map(word_map):
    #sort the map by value
    freq_list = list(word_map.items())
    freq_list.sort(key=lambda x: (-x[1], x[0]))

    print("\n{:15s}{:5s}".format("Word", "Count"))
    print("-" * 20)
    for item in freq_list:
        print("{:15s}{:>5d}".format(item[0], item[1]))


def open_file():
    while True:
        file = input("Enter file name: ")
        try:
            in_file = open(file, "r")
            print()  # keep it for testing purposes in Codio
            break
        except IOError or FileNotFoundError:
            print("\n*** unable to open file ***\n")
            in_file = None

    return in_file


word_map = {}
in_file = open_file()

if in_file != None:
    build_map(in_file, word_map)
    display_map(word_map)
    in_file.close()