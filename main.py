def get_book_text(input):
    with open(input) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(file_contents)

main()
