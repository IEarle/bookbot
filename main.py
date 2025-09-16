import sys
from stats import get_character_frequency, get_word_count, sort_frequencies

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Invalid input")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    frequncies = get_character_frequency(book_text)
    sorted_frequencies = sort_frequencies(frequncies)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for entry in sorted_frequencies:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()