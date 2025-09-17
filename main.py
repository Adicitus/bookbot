import os
import sys
from stats import count_words, count_chars, sort_char_counts

def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        return f.read()

def main(dir_path):
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print(f"Analyzing book found at {book_path}...")

    book_path_full = f"{dir_path}/{book_path}"
    s = get_book_text(book_path_full)
    word_count = count_words(s)
    char_counts = count_chars(s)
    chars_list = sort_char_counts(char_counts)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_record in chars_list:
        c = char_record["char"]
        if c.isalpha():
            print(f"{c}: {char_record["num"]}")
    print("============= END ===============")

if (__name__ == "__main__"):
    main(os.path.dirname(__file__))