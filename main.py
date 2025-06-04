from stats import get_num_words, sorted_lst
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(sys.argv[1])
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_lst(sys.argv[1])
    print("============= END ===============")


main()
