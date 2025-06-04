from stats import get_num_words, sorted_lst


def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = get_num_words()
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_lst()
    print("============= END ===============")


main()
