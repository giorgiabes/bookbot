def character_count():
    text = get_text("books/frankenstein.txt").lower()
    my_dict = {}
    for char in text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


def get_num_words():
    text = get_text("books/frankenstein.txt")
    num_words = len(text.split())
    return f"{num_words} words found in the document"


def get_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text
