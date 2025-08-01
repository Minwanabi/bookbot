import sys
from stats import count_words

from stats import count_letters
from stats import sort_dictionary


def main():
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book {sys.argv[1]}...")
    print("----------- Word Count ----------")
    word_count = count_words(sys.argv[1])
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count = count_letters(sys.argv[1])
    sorted_dict_desc = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    for i in sorted_dict_desc:
        print(f"{i}: {sorted_dict_desc[i]}")

    print("============= END ===============")


main()

