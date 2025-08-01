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
        file_contents = f.read()
        print(type(file_contents))  # Debugging line
        print("file_contents[0:100] =", file_contents[0:100])  # Debugging line
       
