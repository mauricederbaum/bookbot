import sys



def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text
    

from stats import get_words
from stats import get_characters
from stats import sort_characters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_words(book_text)
    characters = get_characters(book_text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print(f"{num_words} words found in the document")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sort_characters(characters)
    print("============= END ===============")
main()