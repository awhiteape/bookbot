def word_count(words):
    count = 0
    count = len(words.split())
    return count

def main():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    #print(book_contents)
    print(word_count(book_contents))
    
main()