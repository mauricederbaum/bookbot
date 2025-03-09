def get_words(book_text):
    words = book_text.split()
    return len(words)

def get_characters(book_text):
    book_text = book_text.lower()
    characters = {}
    for char in book_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
#    print(f"Debug - total characters processed: {sum(characters.values())}")
#    print(f"Debug - length of book_text: {len(book_text)}")
    return characters

def sort_characters(characters):
    character_list = list(characters.items())
    character_list.sort(reverse=True, key=lambda item: item[1])
    #filtered_list = []
    for char, count in character_list:
        if char.isalpha():
            print(f"{char}: {count}")