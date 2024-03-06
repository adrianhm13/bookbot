def get_count_words(text):
    words = text.split()
    return len(words)


def get_count_chars(text):
    dictionary = {}
    lowered_text = text.lower()

    for letter in lowered_text:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    return dictionary


def get_text(path):
    with open(path) as f:
        return f.read()


def transform_to_list(dictionary):
    list = []

    for k in dictionary:
        if k.isalpha():
            list.append({"char": k, "count": dictionary[k]})

    return list


def sort_on(dictionary):
    return dictionary["count"]


def print_chars_with_count(list):
    for e in list:
        print(f"Character {e["char"]}, total count: {e["count"]}")


def print_words_count(count):
    print(f"Total words in the book: {count}")
    print()


def print_title_book(title):
    print(f"Report of the book: {title.capitalize()}")
    print()


def main():
    title_book = "frankestein"
    text = get_text(f"books/{title_book}.txt")
    count_words = get_count_words(text)

    dictionary_letters = get_count_chars(text)
    list_with_dictionaries = transform_to_list(dictionary_letters)
    list_with_dictionaries.sort(reverse=True, key=sort_on)

    print_title_book(title_book)
    print_words_count(count_words)
    print_chars_with_count(list_with_dictionaries)


main()
