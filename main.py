from stats import get_num_words, get_char_count, sorted_listdict
import sys

def get_book_text(filepath)-> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]
    book_text = get_book_text(book)
    word_count = get_num_words(book_text)
    character_count = sorted_listdict(get_char_count(book_text))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in character_count:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")





main()