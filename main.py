
def create_end_report_line():
    return "--- End report ---"
def create_word_count_line(word_count):
    return f"{word_count} words found in the document"
def create_start_report_line(path):
    return f"--- Begin report of {path} ---"
def create_line(line):
    return f"The '{line["char"]}' character was found {line['count']} times"

def sort_on(dict):
    return dict["count"]

def convert_to_list(chars):
    list = []
    for key in chars:
        list.append({ "char": key, "count": chars[key]})
    list.sort(reverse=True, key=sort_on)
    return list
def count_chars(text):
    chars = {}
    for char in text:
        if char not in chars and char.isalpha():
            chars[char] = 0
        if char in chars:
            chars[char] += 1
    return chars

def count_words(text):
    word_count = text.split(" ")
    return len(word_count)

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        print(create_start_report_line("books/frankenstein.txt"))
        print(create_word_count_line(count_words(file_contents)))
        print("")
        for dict in convert_to_list(count_chars(file_contents.lower())):
            print(create_line(dict))
        print(create_end_report_line())

main()