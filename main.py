def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text
    

"""
def get_words(book_text):
    num_words = 0
    words = book_text.split()
    for w in words:
        num_words += 1
    return num_words
"""
def get_words(book_text):
    words = book_text.split()
    return len(words)

def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = get_words(book_text)
    print(f"{num_words} words found in the document")

main()