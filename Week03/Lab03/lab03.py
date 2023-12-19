VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): \n")

while word != "quit":
    word = word.lower()

    if word == "quit":
        break

    elif word == "":
        # Error message used in Codio test
        print("Can't convert an empty string. Try again.")

    else:
        if word[0] in VOWELS:
            print(word + "way")
        else:
            for i, ch in enumerate(word):
                if ch in VOWELS:
                    break
                else:
                    i=0
            print(word[i:] + word[0:i] + "ay")

    word = input("Enter a word ('quit' to quit): \n")