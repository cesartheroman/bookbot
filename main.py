def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_freq = count_characters(text)
    generate_report(num_words, char_freq, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_dict = {}

    for word in text:
        word = word.lower()
        if word.isalpha():
            if word not in char_dict:
                char_dict[word] = 0
            char_dict[word] += 1

    return char_dict


def sort_on(char_map):
    return char_map["freq"]


def sort_dict(char_map):
    dict_list = []

    for char in char_map:
        dict_list.append({"name": char, "freq": char_map[char]})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list


def generate_report(num_words, char_freq, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    sorted_dict = sort_dict(char_freq)

    for dictionary in sorted_dict:
        print(
            f"The {dictionary['name']} character was found {dictionary['freq']} times"
        )

    print("--- End report ---")


main()
