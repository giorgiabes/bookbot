def get_num_words(filepath):
    with open(filepath) as f:
        text = f.read()
    num_words = len(text.split())
    return f"{num_words} words found in the document" 
