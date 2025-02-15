def main(): #execute functions to locate and open the text and count its words
    path = get_path()
    book = read_book(path)
    count, words = list_of(book)
    count = symbol_count(count, words)
    print(count)

def get_path(): #return the file location
    return "books/frankenstein.txt"

def read_book(loc): #read the file and return its content as a string with lower case
    with open(loc) as f:
        book = f.read()
    return book.lower()

def list_of(b): #seperates the string through spaces and returns the length of the resulting list and the list itself
    string = b.split()
    return len(string), string

def symbol_count(c, w): #count the number of each symbol in the list of words and return as a dictionary
    count = {" ": c-1}
    for word in w:
        for char in word:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    return count

main()