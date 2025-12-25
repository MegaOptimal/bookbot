import sys
from stats import number_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content   

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    frank = get_book_text(sys.argv[1])
    num_words = number_words(frank)
    dict_words = count_characters(frank)
    list_dicts = sort_dict(dict_words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list_dicts:
        print(f"{dict["letter"]}: {dict["num"]}")


main()

