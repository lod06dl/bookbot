from stats import get_word_count 

def get_book_text(book):
  with open(book) as f:
    file_content =  f.read()
    return file_content

def main():
    booksf = './books/frankenstein.txt'
    print(f'{get_word_count(get_book_text(booksf))} words found in the document')

main()

 
