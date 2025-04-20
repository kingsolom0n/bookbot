# Get word count
def get_num_words(text):
    words = text.split()
    return len(words)

# Get character count and convert to lower case
def get_char_count(text):
    letters = list(text.lower())
    char_dict = {}

    for letter in letters:
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1

    return char_dict

# def get_sorted_list(chars_dict):
#     chars_list = []

#     for chars in chars_dict:
#         chars_list.append({"char": chars, "count": chars_dict[chars]})
# #        chars_list.append({chars, chars_dict[chars]})
#     chars_list.sort(key=lambda item: item["count"], reverse=True)
#     return chars_list

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list