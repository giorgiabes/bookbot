def main():
    text = get_book_text("books/frankenstein.txt")
    print(count_words(text))

def count_words(text):
    num_words = len(text.split())
    return f"{num_words} words found in the document" 

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
