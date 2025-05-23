from stats import count_words_in_book, count_chars_in_text, create_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    analyze = sys.argv[1]
    print(f"Analyzing book found at {analyze}...")
    text = get_book_text(analyze)

    print("----------- Word Count ----------")
    print(f"Found {count_words_in_book(text)} total words")

    print("--------- Character Count -------")
    for e in create_list(count_chars_in_text(text)):
        c = e["char"]
        n = e["num"]
        if c.isalpha():
            print(f"{c}: {n}")

    print("============= END ===============")
main()