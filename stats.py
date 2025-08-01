import sys

input = sys.argv[1]

def get_book_text(input):

    with open(input) as f:
        file_contents = f.read()
    return file_contents

def count_words(input):

    file_contents = get_book_text(input)
    words = file_contents.split()
    return len(words)

def count_letters(input):

    with open(input) as f:
        file_contents = f.read() # read the file contents and saves as a string
        file_contents = file_contents.lower() # set to lowercase for uniformity
        dictionary = {}
        for i in file_contents:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
    return dictionary

def sort_dictionary(count_letters):
    sorted(count_letters)           
    return sorted_dict    
