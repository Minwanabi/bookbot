from stats import count_words
from stats import get_book_text
from stats import count_letters

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print("File contents NOT printed")
    word_count = count_words("books/frankenstein.txt")
    print(f"{word_count} words found in the document.")
    letter_count = count_letters("books/frankenstein.txt")
    

main()
