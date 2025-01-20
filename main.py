#create a function that takes a string
#return the number of times each character appears
#create a dictionary of the values as String : Int
def character_count(string):
    characters_dict = {}
    print(string.count('p'))
    print(chr(0x61))
    #adds counts for every alphabet lower case char using ascii vals.
    for i in range(0,26):
        characters_dict[chr(0x61+i)] = string.count(chr(0x61+i))
    #adds the punctuation counts to the dictionary
    space = " "
    period = "."
    questionMark = "?"
    characters_dict[space] = string.count(space)
    characters_dict[period] = string.count(period)
    characters_dict[questionMark] = string.count(questionMark)
    print(characters_dict)
    return characters_dict

def word_count(words):
    count = 0
    count = len(words.split())
    return count

def main():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    #print(book_contents)
    print(word_count(book_contents))
    character_count(book_contents.lower())

main()