


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def sortOn(charDic):
        return charDic.keys()

def count_char(text):
    listString = ''.join(text).lower()
    char = [c for c in listString]
    charDic = {}
    for c in char:
        if c.isalpha():
            if c in charDic:
                charDic[c] += 1
            else:
                charDic[c] = 1
                
    listItems = charDic.items()
    sortedItems = sorted(listItems, key=lambda x:x[1], reverse=True)
    return sortedItems

def createReport(charCount, sorted_dictionary):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{charCount} words found in the document")

    for x,y in sorted_dictionary:
        print(f"The '{x}' character was found {y} times")
    print('--- End report ---')

  
    





   

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    charCount = count_char(text)
    createReport(num_words,charCount)

    
 
    
    
    
   

        
        
            
      
        
    
    
  
    
        
    
    







main()