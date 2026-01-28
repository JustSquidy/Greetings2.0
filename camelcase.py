def camelcase(sentence): # Converts sentence to camelCase for example "display all books" becomes "displayAllBooks"
    title_case = sentence.title() # uppercases the first letter of all words
    upper_camel_case = title_case.replace(" ", "") #removes spaces

    return upper_camel_case[0:1].lower() + upper_camel_case[1:] 

def main ():
    sentence = input("Enter a sentence: ")
    output = camelcase(sentence)

    print(output)

if __name__ == "__main__":
    main()