def main(): #execute functions to locate and open the text and count its words
    path = get_path()
    book = read_book(path)
    words = count(book)
    print(words)

def get_path(): #return the file location
    return "books/frankenstein.txt"

def read_book(loc): #read the file and return its content as a string
    with open(loc) as f:
        return f.read()

def count(b): #seperates the string through spaces and returns the length of the resulting list
    string = b.split()
    # s = [string[i] for i in range(10)]
    # print(s)
    return len(string)

main()