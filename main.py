from stats import get_num_words, get_char_count, chars_dict_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count_dict = get_char_count(text)
    sorted_list = chars_dict_to_sorted_list(char_count_dict)
    print_report(book_path, num_words, sorted_list)    

def print_report(book_path, num_words, sorted_list):
        # Printing report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

# Get book content
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()