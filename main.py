def get_word_count(document):
    count = document.split()
    return len(count)

def create_list(document):
    doc_list = []
    for key, value in document.items():
        temp_dict = {"key": key, "value": value}
        doc_list.append(temp_dict)
    return doc_list

def sort_on_key(dict):
    return dict["value"]

def sort_doc(doc_list):
    doc_list.sort(reverse=True,key=sort_on_key)
    return doc_list


def print_report(file_name, document, word_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    doc_list = create_list(document)
    sorted_doc = sort_doc(doc_list)
    key = "key"
    value = "value"
    for val in sorted_doc:
        if val["key"].isalpha():
            print(f"The '{val[key]}' character was found {val[value]} times")
    
    print("--- End report ---")

    #print(f"The '{key}' character was found {value}")

#create a function that takes a string
#return the number of times each character appears
#create a dictionary of the values as String : Int
def get_chars_dict(text):
    chars_dict = {}
    for character in text:
        if character in chars_dict:
            chars_dict[character] += 1
        else:
            chars_dict[character] = 1
    return chars_dict

def word_count(words):
    count = 0
    count = len(words.split())
    return count

def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as book:
        book_contents = book.read()
    document_dict = get_chars_dict(book_contents.lower())
    word_count = get_word_count(book_contents)
    print_report(file_name, document_dict, word_count)
main()