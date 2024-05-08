def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_letters = get_num_letters(text)
    print(f"{num_letters} words found in the document")


def get_num_letters(text):
    letters = text.lower()
    letter_dict = {}
    for i in letters:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    return letter_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()