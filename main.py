def main(): #execute functions to locate and open the text and count its words
    path = get_path()
    book = read_book(path)
    count = symbol_count(book)
    print(report(count))

def get_path(): #return the file location
    return "books/frankenstein.txt"

def read_book(loc): #read the file and return its content as a string with lower case
    with open(loc) as f:
        book = f.read()
    return book.lower()

def symbol_count(s): #count the number of each symbol in the string and return as a dictionary
    count = {}
    for word in s:
        for char in word:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    return count

def report(count): #return the count of each symbol in a formatted string
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += "77986 words found in the document\n"
    report += "The count of each symbol is as follows:\n"
    report += "\n"
    symbols = []
    for symbol in count:
        if symbol.isalpha(): #abc characters only
            symbols.append({"s":symbol, "c":count[symbol]})#List of dictionaries with symbol and count as keys
    #symbols = sorted(symbols, key=lambda x: x['c'], reverse=True) #this sorts the lists in descending order
    symbols.sort(reverse=True, key=sort_on) #sort the list of dictionaries in descending order
    for s in symbols:
        report += f"'{s['s']}': {s['c']}\n"
    return report

def sort_on(d): #helper function to sort the list of dictionaries
    return d["c"]

main()