import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import character_count
from stats import sorted_list

def main():
    path = sys.argv[1]
    words = get_book_text(path)
    word_count = count_words(words)
    char_count = character_count(words)
    sorting = sorted_list(words)
    print(f"Found {word_count} total words")
    for entry in sorting:
        print(f"{entry['char']}: {entry['count']}")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
