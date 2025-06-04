def sort_on(dict):
    return dict["num"]


def sorted_lst(path):
    lst = []
    for char, num in character_count(path).items():
        if char.isalpha():
            lst.append({"char": char, "num": num})

    lst.sort(reverse=True, key=sort_on)
    for i in lst:
        print(f"{i["char"]}: {i["num"]}")


def character_count(path):
    text = get_text(path).lower()
    my_dict = {}
    for char in text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


def get_num_words(path):
    text = get_text(path)
    num_words = len(text.split())
    return num_words


def get_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text
