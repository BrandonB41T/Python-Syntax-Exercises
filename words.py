def print_upper_words(words):
    """
    Takes list of words,
    prints each word on a separate line and makes all letters uppercase
    """
    for word in words:
        print(word.upper())

def print_upper_e_words(words):
    """
    Takes list of words,
    prints all that start with an "e/E" in all uppercase
    """
    for word in words:
        if word[0] == "e" or word[0] == "E":
            print(word.upper())
        
def print_upper_selected(words, letters):
    """
    Takes list of words,
    takes set of letters,
    prints words starting with those letters in all caps
    """
    for word in words:
        for letter in letters:
            if word[0] == letter:
                print(word.upper())