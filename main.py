def main(): #execute functions to locate and open the text and count its words
    path = get_path()
    book = read_book(path)
    count = symbol_count(book)
    print(count)

def get_path(): #return the file location
    return "books/frankenstein.txt"

def read_book(loc): #read the file and return its content as a string with lower case
    with open(loc) as f:
        book = f.read()
    return book.lower()

def symbol_count(s): #count the number of each symbol in the list of words and return as a dictionary
    count = {}
    for word in s:
        for char in word:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    return count

main()