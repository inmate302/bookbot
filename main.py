def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    #abc = 'abcdefghijklmnopqrstuvwxyz'
    chars_sorted_list = chars_dict_to_sorted_list(num_chars)

    print(f"===== Init Report of {book_path} =====")       
    print(f"{num_words} words found!")
    print(sum(num_chars.values()), "characters found!")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("===== End of report =====")


def word_count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars




def open_book(path):
    with open(path) as f:
        return f.read()
    


main()